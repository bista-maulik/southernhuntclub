# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models
 
class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    storage_type = fields.Many2one('storage.type',string='Storage Type',tracking=1)
