# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    preferred_carrier_id = fields.Many2one('preferred.carrier',
                                           string="Preferred Carrier")
    acc_number = fields.Char(string="Account Number")
    delivery_instruction = fields.Text(string="Delivery Instructions")
    tracking_no = fields.Char(string="Tracking", size=50)

    def unlink(self):
        """
        Override the function to reset the is_invoice_tracking in delivery order.
        :return:
        """
        for rec in self:
            if rec.tracking_no:
                picking_ids = self.env['stock.picking'].search([('tracking_no', 'in', rec.tracking_no.split(','))])
                if len(picking_ids) == len(rec.tracking_no.split(',')):
                    picking_ids.write({'is_invoice_tracking': False})
        return super(AccountMove, self).unlink()

    def button_cancel(self):
        """
        Override the function to reset the is_invoice_tracking in delivery order.
        :return:
        """
        for rec in self:
            if rec.tracking_no:
                picking_ids = self.env['stock.picking'].search([('tracking_no', 'in', rec.tracking_no.split(','))])
                if len(picking_ids) == len(rec.tracking_no.split(',')):
                    picking_ids.write({'is_invoice_tracking': False})
        return super(AccountMove, self).button_cancel()
