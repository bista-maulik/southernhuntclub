# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, api, _


class WorkCenter(models.Model):
    _inherit = "mrp.workcenter"

    wip_account_id = fields.Many2one("account.account", "WIP Account")
    labour_account_id = fields.Many2one("account.account", "Labour Account")
    product_id = fields.Many2one('product.product', domain="[('type','=','service')]", string="Related Product")
