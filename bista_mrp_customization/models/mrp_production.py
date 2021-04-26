# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    backorder_id = fields.Many2one('mrp.production', string="Back Order Of#")
    backorder_ids = fields.One2many('mrp.production', 'backorder_id', string="Back Orders")
    is_wo_processed = fields.Boolean(string="Is Workorders Processed", compute="_compute_workorder_processed")

    @api.depends('workorder_ids')
    def _compute_workorder_processed(self):
        for rec in self:
            rec.is_wo_processed = False
            if rec.workorder_ids and all(
                    wo.state == 'done' for wo in self.workorder_ids):
                rec.is_wo_processed = True


    def _generate_backorder_productions(self, close_mo=True):
        backorders = super(MrpProduction, self)._generate_backorder_productions(close_mo=close_mo)
        if backorders:
            backorders.write({'backorder_id': self.id})
            if any(move.state not in ('draft', 'done', 'cancel') for move in backorders.move_raw_ids):
                if backorders.move_raw_ids.mapped('move_line_ids'):
                    backorders.move_raw_ids.mapped('move_line_ids').filtered(lambda x: x.qty_done > 0).write({'qty_done': 0.0})
                backorders.move_raw_ids._do_unreserve()
                backorders.move_raw_ids.write({'state': 'draft'})
                backorders.button_unplan()
        return backorders
