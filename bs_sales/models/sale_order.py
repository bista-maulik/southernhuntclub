# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError
# from datetime import datetime, timedelta
from datetime import datetime



class SaleOrder(models.Model):
    _inherit = "sale.order"

    sales_rep = fields.Many2one('sales.rep',string='Sales Rep',domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",tracking=1)
    cancellation_date = fields.Datetime('Cancellation Date', copy=False,tracking=1)
    commitment_date = fields.Datetime('Delivery Date', copy=False,
                                      states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
                                      help="This is the delivery date promised to the customer. "
                                           "If set, the delivery order will be scheduled based on "
                                           "this date rather than product lead times."
                                           ,default=lambda self: fields.datetime.now())

    
   

    
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

        
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def set_product_quantity(self,qty):
        qty_data=str(qty)
        qty_data1 = str(qty).split('.')[1]
        qty_data2 = str(qty).split('.')[0]
        if int(qty_data1) ==0:
            return qty_data2
        else:
            return qty_data
       
       

