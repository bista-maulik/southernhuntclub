# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    sales_rep = fields.Many2one('sales.rep',string='Sales Rep',required=True,tracking=1)
    is_a_customer = fields.Boolean(string="Is a Customer", default=True,  help="Check this box if this contact is a customer.")
    is_a_vendor = fields.Boolean(string="Is a Vendor",help="Check this box if this contact is a vendor. ")

  
    @api.model
    def fields_get(self, fields=None):
        hide = ['user_id']
        res = super(ResPartner, self).fields_get()
        for field in hide:
            res[field]['searchable'] = False   #hide from filter
            res[field]['sortable'] = False #hide from group by
        return res
