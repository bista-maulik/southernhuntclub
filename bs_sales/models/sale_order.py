# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api, _



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
    total_cost = fields.Float(string="Total Cost", store=True, readonly=True, compute="_compute_total_cost")

    @api.depends('order_line.purchase_price', 'order_line.qty_delivered')
    def _compute_total_cost(self):
        """
        Define function to set cost.
        :return:
        """
        for rec in self:
            total_cost = 0.0
            for line in rec.order_line:
                total_cost += line.purchase_price * line.qty_delivered
            rec.update({'total_cost': total_cost})

    @api.model
    def default_get(self, fields):
        """
        Override function to change the picking policy value.
        :param fields:
        :return:
        """
        res = super(SaleOrder, self).default_get(fields)
        res['picking_policy'] = 'one'
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

        
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    color = fields.Char(related="product_id.color", string="Color")
    upc = fields.Char(related="product_id.upc", string="UPC")

    def set_product_quantity(self,qty):
        qty_data=str(qty)
        qty_data1 = str(qty).split('.')[1]
        qty_data2 = str(qty).split('.')[0]
        if int(qty_data1) ==0:
            return qty_data2
        else:
            return qty_data
