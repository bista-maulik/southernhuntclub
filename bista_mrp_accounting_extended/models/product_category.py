# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    property_mrp_stock_account_input_categ_id = fields.Many2one(
        'account.account', 'MRP Stock Input Account', company_dependent=True,
        domain="[('company_id', '=', allowed_company_ids[0]), ('deprecated', '=', False)]", check_company=True,
        help="""When doing automated inventory valuation for Manufacturing Orders, counterpart journal items for all incoming stock moves will be posted in this account,
                unless there is a specific valuation account set on the source location. This is the default value for all products in this category.
                It can also directly be set on each product.""")
    property_mrp_stock_account_output_categ_id = fields.Many2one(
        'account.account', 'MRP Stock Output Account', company_dependent=True,
        domain="[('company_id', '=', allowed_company_ids[0]), ('deprecated', '=', False)]", check_company=True,
        help="""When doing automated inventory valuation for Manufacturing Orders., counterpart journal items for all outgoing stock moves will be posted in this account,
                unless there is a specific valuation account set on the destination location. This is the default value for all products in this category.
                It can also directly be set on each product.""")
