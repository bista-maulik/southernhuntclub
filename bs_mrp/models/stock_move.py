# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    product_onhand_qty = fields.Float(related='product_id.qty_available',
                                      string="Product Onhand Qty")
    product_available_qty = fields.Float(string="Product Available Qty",
                                         compute='_compute_available_qty')

    def _compute_available_qty(self):
        """
        Define compute function to calculate the available quantity for
        components.
        :return:
        """
        for rec in self:
            if rec.product_id:
                rec.product_available_qty = round(0.0000, 4)
                domain_quant_loc, domain_move_in_loc, domain_move_out_loc = rec.product_id._get_domain_locations()
                quant_domain = [('product_id', 'in', rec.product_id.ids)] + domain_quant_loc
                quants = self.env['stock.quant'].search(quant_domain)
                if quants:
                    rec.product_available_qty = round(
                        sum(quants.mapped('available_quantity')), 4)
