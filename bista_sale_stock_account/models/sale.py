# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    preferred_carrier_id = fields.Many2one('preferred.carrier',
                                           string="Preferred Carrier")
    acc_number = fields.Char(string="Account Number")
    delivery_instruction = fields.Char(string="Delivery Instructions")

    def _prepare_invoice(self):
        """
        Override function to set delivery data in invoice.
        :return:
        """
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        picking_id = self.env['stock.picking']
        if self.picking_ids:
            picking = self.picking_ids.filtered(lambda l: not l.is_invoice_tracking and l.state == 'done')
            if picking:
                picking_id = picking
            else:
                picking = self.picking_ids.filtered(lambda l:l.is_invoice_tracking and l.state == 'done')
                if picking:
                    picking_id = picking[0]
        if picking_id:
            tracking_no = picking_id[0].tracking_no
            data_vals = {
                'preferred_carrier_id': picking_id[0].preferred_carrier_id and picking_id[0].preferred_carrier_id.id or False,
                'acc_number': picking_id[0].acc_number,
                'delivery_instruction': picking_id[0].delivery_instruction,
            }
            if len(picking_id) > 1:
                tracking_no = ','.join([str(elem) for elem in picking_id.mapped('tracking_no') if elem])
            data_vals.update({
                'tracking_no': tracking_no
            })
            invoice_vals.update(data_vals)
            picking_id.write({'is_invoice_tracking': True})
        return invoice_vals
