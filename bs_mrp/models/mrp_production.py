# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api, _
 
class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    storage_type = fields.Many2one('storage.type',string='Storage Type',tracking=1)
    
    @api.onchange('bom_id')
    def _onchange_bom_id_set_storage_type(self):
        for order in self: 
            if order.bom_id:
                order.storage_type = order.bom_id.storage_type
