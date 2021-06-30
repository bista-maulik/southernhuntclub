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
    backorder_ids = fields.One2many(
        'mrp.production', 'backorder_id', string="Back Orders")
    is_wo_processed = fields.Boolean(
        string="Is Workorders Processed", compute="_compute_workorder_processed")
    is_transfer_pending = fields.Boolean(
        string="Is Transfer Pending", compute="_compute_is_transfer_pending")

    @api.depends('picking_ids')
    def _compute_is_transfer_pending(self):
        """
        Define compute function which check any transfer is on pending or not.
        :return:
        """
        for rec in self:
            is_transfer_pending = False
            if rec.picking_ids and any(picking_id.state != 'done' for picking_id in rec.picking_ids):
                is_transfer_pending = True
            rec.is_transfer_pending = is_transfer_pending

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
            if production.state == 'to_close':
                if any(wo.state == 'ready' for wo in production.workorder_ids) and all(
                        wo.state != 'done' for wo in production.workorder_ids):
                    production.state = 'confirmed'
                elif not all(wo_state in ('done', 'cancel') for wo_state in production.workorder_ids.mapped('state')):
                    production.state = 'progress'
            elif production.state == 'progress' and all(wo.state in ('done', 'cancel') for wo in production.workorder_ids):
                production.state = 'to_close'

    def button_mark_done(self):
        """
        Override the function to add pop-up of the confirmation based on transfers
        done or not.
        :return:
        """

        # added loop for subcontracting singleton issue.
        for rec in self:
            if rec.is_transfer_pending and not self._context.get('confirmation', False):
                return {
                    'name': "Manufacturing Confirmation",
                    'res_model': 'wizard.mo.confirmation',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'view_type': 'form',
                    'view_id': self.env.ref(
                        'bista_mrp_customization.view_wizard_mo_confirmation_form').id,
                    'target': 'new',
                    'context': {'default_production_id': rec.id}
                }
        return super(MrpProduction, self).button_mark_done()

    def _generate_backorder_productions(self, close_mo=True):
        """
        Override function to make changes in backorder and set as new
        manufacturing order.
        :param close_mo:
        :return:
        """
        backorders = super(MrpProduction, self)._generate_backorder_productions(close_mo=close_mo)
        if backorders:
            if len(self) > 1:
                for rec in self:
                    if rec.procurement_group_id.mrp_production_ids and (
                            rec.procurement_group_id.mrp_production_ids - rec in backorders):
                        backorder = rec.procurement_group_id.mrp_production_ids - rec
                        backorder.write({'backorder_id': rec.id})
            else:
                backorders.write({'backorder_id': self.id})
            if any(move.state not in ('draft', 'done', 'cancel') for move in backorders.move_raw_ids):
                if backorders.move_raw_ids.mapped('move_line_ids'):
                    backorders.move_raw_ids.mapped('move_line_ids').filtered(lambda x: x.qty_done > 0).write({'qty_done': 0.0})
                backorders.move_raw_ids._do_unreserve()
                backorders.move_raw_ids.write({'state': 'draft'})
                backorders.button_unplan()
                backorders.write({'qty_producing': 0.0})
        return backorders
