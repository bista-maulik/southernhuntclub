# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, _
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_accounting_data_for_valuation(self):
        """
        Inherit the function to change source account and dest account from
        product categories for the journal entry.
        :return:
        """
        journal_id, acc_src, acc_dest, acc_valuation = super(StockMove, self)._get_accounting_data_for_valuation()
        production_id = self.production_id
        raw_material_production_id = self.raw_material_production_id
        if production_id or raw_material_production_id:
            product_categ_id = self.product_id.categ_id
            property_mrp_stock_account_input_categ_id = product_categ_id.property_mrp_stock_account_input_categ_id
            property_mrp_stock_account_output_categ_id = product_categ_id.property_mrp_stock_account_output_categ_id
            if property_mrp_stock_account_input_categ_id and property_mrp_stock_account_output_categ_id:
                acc_src = property_mrp_stock_account_input_categ_id.id
                acc_dest = property_mrp_stock_account_output_categ_id.id
        return journal_id, acc_src, acc_dest, acc_valuation
