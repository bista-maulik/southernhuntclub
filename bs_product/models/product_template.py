# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import api, fields, models, tools, _

class ProductTemplate(models.Model):
    _inherit = "product.template"
   
    color = fields.Char("Color",tracking=1)
    upc = fields.Char("UPC",tracking=1)
        