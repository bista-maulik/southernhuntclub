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
        """
        Define compute method to set is_wo_processed field value.
        :return:
        """
        for rec in self:
            rec.is_wo_processed = False
            if rec.workorder_ids and all(
                    wo.state == 'done' for wo in self.workorder_ids):
                rec.is_wo_processed = True

    @api.depends(
        'move_raw_ids.state', 'move_raw_ids.quantity_done',
        'move_finished_ids.state',
        'workorder_ids', 'workorder_ids.state', 'product_qty', 'qty_producing')
    def _compute_state(self):
        """
        Override the function to improvement in state of manufacturing.
        :return:
        """
        super(MrpProduction, self)._compute_state()
        for production in self:
            if production.state == 'to_close' and not all(wo_state in ('done', 'cancel') for wo_state in production.workorder_ids.mapped('state')):
                production.state = 'progress'

    def _generate_backorder_productions(self, close_mo=True):
        """
        Override function to make changes in backorder and set as new
        manufacturing order.
        :param close_mo:
        :return:
        """
        backorders = super(MrpProduction, self)._generate_backorder_productions(close_mo=close_mo)
        if backorders:
            backorders.write({'backorder_id': self.id})
            if any(move.state not in ('draft', 'done', 'cancel') for move in backorders.move_raw_ids):
                if backorders.move_raw_ids.mapped('move_line_ids'):
                    backorders.move_raw_ids.mapped('move_line_ids').filtered(lambda x: x.qty_done > 0).write({'qty_done': 0.0})
                backorders.move_raw_ids._do_unreserve()
                backorders.move_raw_ids.write({'state': 'draft'})
                backorders.button_unplan()
                backorders.write({'qty_producing': 0.0})
        return backorders
