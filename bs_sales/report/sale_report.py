
from odoo import tools
from odoo import api, fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"
    
    sales_rep = fields.Many2one('sales.rep',string='Sales Rep', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['sales_rep'] = ", s.sales_rep as sales_rep"
        groupby += ', s.sales_rep'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)

    @api.model
    def fields_get(self, fields=None):
        hide = ['user_id']
        res = super(SaleReport, self).fields_get()
        for field in hide:
            res[field]['searchable'] = False   #hide from filter
            res[field]['sortable'] = False #hide from group by
        return res



