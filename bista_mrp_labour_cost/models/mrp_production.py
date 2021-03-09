# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    def get_count_journal_entries(self):
        """
        Define compute function which calculate the account move which set the
        production.
        :return:
        """
        for record in self:
            move_ids = self.env['account.move'].search([('production_id', '=', record.id)])
            record.count_journal_entries = len(move_ids.ids)

    count_journal_entries = fields.Integer(compute='get_count_journal_entries', string='Count Journal Entries')

    def _post_inventory(self, cancel_backorder=False):
        """
        Create Journal entry for Labour cost for employee
        :param cancel_backorder:
        :return:
        """
        AccountMove = self.env['account.move']
        for wc_line in self.workorder_ids:
            workcenter_hrs_qty = 0
            workcenter_cost = 0
            for wc_time_id in wc_line.time_ids:
                duration = wc_time_id.duration
                workcenter_hrs_qty += (duration / 60)
                workcenter_cost += (duration / 60) * wc_line.workcenter_id.costs_hour

            wc_product = wc_line.workcenter_id.product_id
            if not wc_product:
                raise UserError(
                    "Please configure 'Labour' Product in System and Configure in Corresponding Workcenter or Contact System Administrator !!!")
            if not wc_line.workcenter_id.wip_account_id:
                raise UserError(
                    "Please configure 'WIP Account' Corresponding Workcenter or Contact System Administrator !!!")
            if not wc_line.workcenter_id.labour_account_id:
                raise UserError(
                    "Please configure 'Labour Account' Corresponding Workcenter or Contact System Administrator !!!")

            if wc_product and wc_line.workcenter_id.wip_account_id and wc_line.workcenter_id.labour_account_id:
                wc_debit_account_id = wc_line.workcenter_id.wip_account_id.id
                wc_credit_account_id = wc_line.workcenter_id.labour_account_id.id

                debit_line_vals = {
                    'name': self.name,
                    'product_id': wc_product.id,
                    'quantity': workcenter_hrs_qty,
                    'product_uom_id': wc_product.uom_id.id,
                    'ref': self.origin,
                    'debit': workcenter_cost if workcenter_cost > 0 else 0,
                    'credit': -workcenter_cost if workcenter_cost < 0 else 0,
                    'account_id': wc_debit_account_id,
                }
                credit_line_vals = {
                    'name': self.name,
                    'product_id': wc_product.id,
                    'quantity': workcenter_hrs_qty,
                    'product_uom_id': wc_product.uom_id.id,
                    'ref': self.origin,
                    'credit': workcenter_cost if workcenter_cost > 0 else 0,
                    'debit': -workcenter_cost if workcenter_cost < 0 else 0,
                    'account_id': wc_credit_account_id,
                    }
                move_lines = [(0, 0, debit_line_vals),
                              (0, 0, credit_line_vals)]
                if move_lines:
                    date = self._context.get('force_period_date', fields.Date.context_today(self))
                    accounts_data = self.product_id.product_tmpl_id.get_product_accounts()
                    journal_id = accounts_data['stock_journal'].id
                    wc_account_move = AccountMove.sudo().create({
                        'journal_id': journal_id,
                        'line_ids': move_lines,
                        'date': date,
                        'ref': self.name + 'Workcenter Cost',
                        'production_id': self.id,
                    })
                    wc_account_move._post(soft=False)
        return super(MrpProduction, self)._post_inventory(cancel_backorder=cancel_backorder)

    def redirect_to_account_move(self):
        """
        Define the function which redirect you in journal entry which created
        for the manufacturing order.
        :return:
        """
        [action] = self.env.ref('account.action_move_journal_line').sudo().read()
        for order in self:
            context = self._context.copy()
            action['domain'] = [('production_id', '=', order.id)]
            context.update({'create': False})
            action['context'] = context
            return action


class AccountMove(models.Model):
    _inherit = "account.move"

    production_id = fields.Many2one('mrp.production', 'Production')
