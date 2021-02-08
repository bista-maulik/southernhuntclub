# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sales_rep = fields.Many2one('sales.rep',string='Sales Rep',domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",tracking=1)
    cancellation_date = fields.Datetime('Cancellation Date', copy=False,tracking=1)

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
           if not order.commitment_date:
               order.commitment_date = fields.datetime.now()
        return res


    @api.onchange('partner_id')
    def _onchange_partner_id_set_sale_rep(self):
        for order in self: 
            if order.partner_id:
                order.sales_rep = order.partner_id.sales_rep

       
    @api.model
    def fields_get(self, fields=None):
        hide = ['user_id']
        res = super(SaleOrder, self).fields_get()
        for field in hide:
            res[field]['searchable'] = False   #hide from filter
            res[field]['sortable'] = False #hide from group by
        return res

        
