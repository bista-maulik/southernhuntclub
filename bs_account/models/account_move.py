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

    total_cost = fields.Float(string="Total Cost",
                              compute="_compute_total_cost")

    @api.depends('invoice_line_ids')
    def _compute_total_cost(self):
        """
        Define the function to set cost.
        :return:
        """
        for rec in self:
            total_cost = 0.0
            for invoice_line in rec.invoice_line_ids:
                so_line = invoice_line.sale_line_ids.filtered(lambda l: l.product_id == invoice_line.product_id)
                if so_line:
                    total_cost += so_line[0].purchase_price * invoice_line.quantity
            rec.update({'total_cost': total_cost})


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def set_product_quantity(self, qty):
        qty_data = str(qty)
        qty_data1 = str(qty).split('.')[1]
        qty_data2 = str(qty).split('.')[0]
        if int(qty_data1) == 0:
            return qty_data2
        else:
            return qty_data
