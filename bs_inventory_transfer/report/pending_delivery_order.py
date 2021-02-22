# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import tools
from odoo import api, fields, models,_
 

class PendingDeliveryOrderReport(models.Model):
    _name = "pending.delivery.orders.report"
    _description = "Pending Delivery Orders Report"
    _auto = False
    _order = 'delivery_date desc'

    id = fields.Integer('Id')
    sale_id = fields.Many2one('sale.order','Sales Ord. #', readonly=True)
    partner_id = fields.Many2one('res.partner', 'Customer', readonly=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    delivery_date = fields.Datetime('Delivery Date', readonly=True)
    pending_qty = fields.Float('Pending Qty.', readonly=True)
    available_qty = fields.Float('Available Qty.', readonly=True)
    on_hand_qty = fields.Float(related='product_id.qty_available',string='On Hand Qty.')
    company_id = fields.Many2one('res.company', 'Company', readonly=True)

    def _select(self):
        return """
            SELECT
            row_number() over (partition by true ) as id,
            sp.sale_id as sale_id,
            so.partner_id as partner_id,
            sml.product_id as product_id,
            so.commitment_date as delivery_date,
            sml.company_id as company_id,
            (select (sum(quantity) - sum(reserved_quantity) )  from stock_quant where product_id =sml.product_id and quantity >0) as available_qty,
            case when (sml.product_uom_qty-sml.qty_done) < 0 then 0 else (product_uom_qty-qty_done) end as pending_qty
        """

    def _from(self):
        return """
            from stock_move_line sml inner join 
            stock_picking sp on (sp.id=sml.picking_id)
            left join stock_quant sq on (sq.product_id=sml.product_id)
            left join sale_order so on (so.id=sp.sale_id)
        """

    def _where(self):
        return """
            where (sml.product_uom_qty- sml.qty_done) > 0
            --or (sq.quantity-sq.reserved_quantity) > 0
        """ 

    def _groupby(self):
        return """
            group by so.partner_id,sp.sale_id,so.commitment_date,sml.product_id,sml.company_id,sml.product_uom_qty,sml.qty_done,sml.id
            --,sq.quantity,sq.reserved_quantity
         """

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                %s
                %s
                %s
                %s
            )
        """ % (self._table, self._select(), self._from(), self._where(), self._groupby())
        )

        




    
    
