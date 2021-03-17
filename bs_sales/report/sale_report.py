# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import tools
from odoo import api, fields, models

class SaleReport(models.Model):
    _inherit = "sale.report"
    
    sales_rep = fields.Many2one('sales.rep',string='Sales Rep', readonly=True)
    commitment_date = fields.Datetime('Delivery Date', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['sales_rep'] = ", s.sales_rep as sales_rep"
        fields['commitment_date'] = ", s.commitment_date as commitment_date"
        groupby += ', s.sales_rep'
        groupby +=', s.commitment_date'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)

    @api.model
    def fields_get(self, fields=None):
        hide = ['user_id']
        res = super(SaleReport, self).fields_get()
        for field in hide:
            res[field]['searchable'] = False   #hide from filter
            res[field]['sortable'] = False #hide from group by
        return res



