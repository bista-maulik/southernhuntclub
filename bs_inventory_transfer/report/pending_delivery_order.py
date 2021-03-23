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
    _table = 'pending_delivery_orders_report'

    id = fields.Integer('Id')
    name = fields.Char('Name', readonly=True,index=True)
    state = fields.Selection([
        ('draft', 'New'), ('cancel', 'Cancelled'),
        ('waiting', 'Waiting Another Move'),
        ('confirmed', 'Waiting Availability'),
        ('partially_available', 'Partially Available'),
        ('assigned', 'Available'),
        ('done', 'Done')], string='Status',
        index=True, readonly=True,
        help="* New: When the stock move is created and not yet confirmed.\n"
                "* Waiting Another Move: This state can be seen when a move is waiting for another one, for example in a chained flow.\n"
                "* Waiting Availability: This state is reached when the procurement resolution is not straight forward. It may need the scheduler to run, a component to be manufactured...\n"
                "* Available: When products are reserved, it is set to \'Available\'.\n"
                "* Done: When the shipment is processed, the state is \'Done\'.")
                
    picking_type_id = fields.Many2one('stock.picking.type', 'Operation Type',readonly=True,index=True)
    sale_id = fields.Many2one('sale.order','Sales Ord. #', readonly=True,index=True)
    sale_price = fields.Float(string="Price", readonly=True, index=True)
    partner_id = fields.Many2one('res.partner', 'Customer', readonly=True,index=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True,index=True)
    delivery_date = fields.Datetime('Delivery Date', readonly=True,index=True)
    pending_qty = fields.Float('Pending Qty.', readonly=True,index=True)
    
    # on_hand_qty = fields.Float(related='product_id.qty_available',string='On Hand Qty.')
    # available_qty = fields.Float(related='product_id.virtual_available',string='Available Qty.')
    on_hand_qty = fields.Float(string='On Hand Qty.',  group_operator='avg')
    # available_qty = fields.Float(string='Available Qty.')

    company_id = fields.Many2one('res.company', 'Company', readonly=True,index=True)
    move_id = fields.Many2one('stock.move', 'MoveId', readonly=True,index=True)
    # product_qty = fields.Float(related='move_id.forecast_availability',string='Reserved Qty.', readonly=True,index=True)

    def _select(self):
        return """
            SELECT
                row_number() over (partition by true ) as id
                ,sp.name as name
                ,sm.state as state
                ,sp.picking_type_id as picking_type_id
                ,sp.sale_id as sale_id
                ,sol.price_subtotal as sale_price
                --,so.partner_id as partner_id
                ,case when so.partner_id notnull then so.partner_id else sp.partner_id end as "partner_id"
                ,sm.product_id as product_id
                --,(sml.product_uom_qty-sml.qty_done) as pending_qty
                ,sm.product_uom_qty as pending_qty
                ,sm.date_deadline as delivery_date
               -- ,(sq.quantity - sq.reserved_quantity) as available_qty
                --,sq.quantity as on_hand_qty
                --,sm.product_qty
                ,sm.company_id as company_id
                ,sm.id as move_id
                ,(select sum(quantity) from stock_quant sq left join stock_location sl on sl.id = sq.location_id where sl.usage = 'internal' and sq.product_id=sm.product_id) as on_hand_qty
                --,(select (quantity - reserved_quantity) from stock_quant where (location_id=sp.location_id and company_id=sm.company_id) and product_id=sm.product_id) as available_qty

                 """

    def _from(self):
        return """
            from stock_move sm 
            inner join stock_picking_type spt on 
            spt.id = sm.picking_type_id 
            left join (select  product_id ,quantity,reserved_quantity from stock_quant where quantity > 0) sq on sq.product_id=sm.product_id
            left join sale_order_line sol on sol.id=sm.sale_line_id
            left join sale_order so on so.id=sol.order_id  
            left join stock_picking sp on sp.id=sm.picking_id
            left join stock_move_line sml on sml.move_id = sm.id
        """

    def _where(self):
        return """
         where (code ='outgoing' and active='t')  and sm.product_uom_qty > 0 and sm.state not in ('done','cancel')
         
        """ 

    def _groupby(self):
        return """
         group by 
            sq.product_id
            ,sm.product_id
            ,sol.id
            ,sm.date_deadline
            ,sm.product_uom_qty
            ,sm.picking_type_id
            ,sm.company_id
            ,sm.picking_id
            ,sm.sale_line_id
            ,sp.sale_id
            ,so.partner_id
            ,sp.partner_id
            ,sp.name
            ,sm.state
            --,sml.product_uom_qty
            --,sml.qty_done
            ,sp.picking_type_id
            --,sq.quantity
            --,sq.reserved_quantity
            --,sm.product_qty
            ,sm.id
            ,sp.location_id
         """

    def init(self):
        self._cr.execute("DROP view IF EXISTS %s CASCADE" % (self._table))
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                %s
                %s
                %s
                %s
            )
        """ % (self._table, self._select(), self._from(), self._where(), self._groupby())
        )
