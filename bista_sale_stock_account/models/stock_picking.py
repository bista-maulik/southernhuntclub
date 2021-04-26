# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    preferred_carrier_id = fields.Many2one('preferred.carrier',
                                           string="Preferred Carrier")
    acc_number = fields.Char(string="Account Number")
    delivery_instruction = fields.Char(string="Delivery Instructions")
    tracking_no = fields.Char(string="Tracking", copy=False)
    is_invoice_tracking = fields.Boolean(string="Set Tracking in Invoice")
