# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api, _

class StorageType(models.Model):
    _name = "storage.type"
    _description = "Storage Type"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _check_company_auto = True


    name = fields.Char(string="Name",required=True,tracking=1)
    description = fields.Char(string='Description',required=True,tracking=1)
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company,tracking=1)


