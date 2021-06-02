# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    total_cost = fields.Float(string="Total Cost", store=True, readonly=True,
                              compute="_compute_total_cost")

    @api.depends('invoice_line_ids')
    def _compute_total_cost(self):
        """
        Define the function to set cost.
        :return:
        """
        for rec in self:
            total_cost = sum(rec.invoice_line_ids.mapped('line_cost'))
            rec.update({'total_cost': total_cost})


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    line_cost = fields.Float(string="Line Cost", store=True, readonly=True,
                             compute="_compute_line_cost")

    @api.depends('sale_line_ids', 'quantity')
    def _compute_line_cost(self):
        """
        Define compute function to calculate line_cost.
        :return:
        """
        for invoice_line in self:
            line_cost = 0.0
            so_line = invoice_line.sale_line_ids.filtered(lambda l: l.product_id == invoice_line.product_id)
            if so_line:
                line_cost += so_line[0].purchase_price * invoice_line.quantity
            invoice_line.line_cost = line_cost


    def set_product_quantity(self, qty):
        qty_data = str(qty)
        qty_data1 = str(qty).split('.')[1]
        qty_data2 = str(qty).split('.')[0]
        if int(qty_data1) == 0:
            return qty_data2
        else:
            return qty_data
