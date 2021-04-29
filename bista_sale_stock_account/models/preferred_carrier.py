# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields


class SaleOrder(models.Model):
    _name = "preferred.carrier"
    _description = "Preferred Carrier"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
