# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import api, fields, models

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def set_product_quantity(self,qty):
        qty_data=str(qty)
        qty_data1 = str(qty).split('.')[1]
        qty_data2 = str(qty).split('.')[0]
        if int(qty_data1) ==0:
            return qty_data2
        else:
            return qty_data