# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api, _
from datetime import datetime, timedelta


class StockPicking(models.Model):
    _inherit = 'stock.picking'
        
    cancellation_date = fields.Datetime('Cancellation Date', copy=False, store=True, readonly=False,related="group_id.sale_id.cancellation_date",tracking=1)
    date_order = fields.Datetime('Order Date', copy=False, store=True, readonly=False,related="group_id.sale_id.date_order",tracking=1)
    
    @api.depends('move_lines.state', 'move_lines.date', 'move_type')
    def _compute_scheduled_date(self):
        res = super(StockPicking, self)._compute_scheduled_date()
        for picking in self:
            if picking.sale_id:
                picking.scheduled_date = picking.sale_id.commitment_date
        return res



   

 






    

