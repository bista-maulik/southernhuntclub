# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        """
        Override function to set delivery tab data in invoice.
        :param order:
        :param name:
        :param amount:
        :param so_line:
        :return:
        """
        vals = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(
            order=order, name=name, amount=amount, so_line=so_line)
        picking_id = self.env['stock.picking']
        if order.picking_ids:
            picking = order.picking_ids.filtered(
                lambda l: not l.is_invoice_tracking and l.state == 'done')
            if picking:
                picking_id = picking[0]
            else:
                picking = order.picking_ids.filtered(
                    lambda l: l.is_invoice_tracking and l.state == 'done')
                if picking:
                    picking_id = picking[-1]
        if picking_id:
            vals.update({
                'preferred_carrier_id': picking_id.preferred_carrier_id and picking_id.preferred_carrier_id.id or False,
                'acc_number': picking_id.acc_number,
                'delivery_instruction': picking_id.delivery_instruction,
                'tracking_no': picking_id.tracking_no,
            })
        return vals
