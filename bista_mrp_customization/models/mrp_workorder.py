# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models
from odoo.osv import expression
from odoo.exceptions import UserError


class MrpWorkorder(models.Model):
    _inherit = "mrp.workorder"

    def button_start(self):
        """
        Override function to check validation based on configuration and
        conditions.
        :return:
        """
        if self.env['ir.config_parameter'].sudo().get_param(
                'bista_mrp_customization.is_transfer_process_validation'):
            if self.production_id.picking_ids and any(
                    picking.state not in ('done', 'cancel') for picking in self.production_id.picking_ids):
                raise UserError(
                    "You cannot process the workorder without all Transfers Done, Please process the Transfers first!")
        return super(MrpWorkorder, self).button_start()

    def record_production(self):
        """
        Override the function to return the exact view based on condition.
        :return:
        """
        action = super(MrpWorkorder, self).record_production()
        if self.production_id.backorder_ids and self.production_id.backorder_ids.workorder_ids:
            backorder_workorders = self.production_id.backorder_ids.workorder_ids
            backorder_workorders.mapped('time_ids').unlink()
            backorder_workorders.mapped('leave_id').unlink()
            backorder_workorders.write({
                'date_planned_start': False,
                'date_planned_finished': False,
                'state': 'ready',
            })
        if action is not True and self.production_id.backorder_ids:
            if self.production_id.workorder_ids and self.production_id.workorder_ids.filtered(
                    lambda l: l.state not in ('done', 'cancel', 'pending')):
                domain = [('state', 'not in', ['done', 'cancel', 'pending'])]
                action = self.env["ir.actions.actions"]._for_xml_id("mrp.action_mrp_workorder_production_specific")
                action['domain'] = expression.AND([domain, [('production_id','=',self.production_id.id)]])
                action['target'] = 'main'
            else:
                action = self.env["ir.actions.actions"]._for_xml_id(
                    "mrp.mrp_workcenter_kanban_action")
                action['target'] = 'main'
        elif action is True and self.production_id.workorder_ids:
            if not any(self.production_id.workorder_ids.filtered(lambda l: l.state not in ('done', 'cancel'))):
                action = self.env["ir.actions.actions"]._for_xml_id(
                    "mrp.mrp_workcenter_kanban_action")
                action['target'] = 'main'
        return action
