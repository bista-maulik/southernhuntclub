# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import api, fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    total_cost = fields.Float(string='Total Cost', readonly=True)


    @api.model
    def _select(self):
        """
        Override function to add total cost in analysis report.
        :return:
        """
        query = super(AccountInvoiceReport, self)._select()
        query += ", line.line_cost  AS total_cost"
        return query
