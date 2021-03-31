# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, api


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    @api.depends('payment_type',
                 'journal_id.inbound_payment_method_ids',
                 'journal_id.outbound_payment_method_ids')
    def _compute_payment_method_id(self):
        """
        Override the function to change the payment method in invoice to
        Batch Payment and vendor bill to Checks.
        :return:
        """
        super(AccountPaymentRegister, self)._compute_payment_method_id()
        for wizard in self:
            payment_method_id = False
            if wizard.payment_type == 'inbound':
                payment_method_id = self.env.ref('account_batch_payment.account_payment_method_batch_deposit').id
            else:
                payment_method_id = self.env.ref('account_check_printing.account_payment_method_check').id
            if payment_method_id and payment_method_id in wizard.available_payment_method_ids.ids:
                payment_method_id = self.env['account.payment.method'].browse(payment_method_id)
                wizard.payment_method_id = payment_method_id
