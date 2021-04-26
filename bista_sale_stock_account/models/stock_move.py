# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_new_picking_values(self):
        """
        Override function to set the delivery tab data in delivery order.
        :return:
        """
        vals = super(StockMove, self)._get_new_picking_values()
        if self.group_id.sale_id:
            vals.update({
                'preferred_carrier_id': self.group_id.sale_id.preferred_carrier_id and self.group_id.sale_id.preferred_carrier_id.id or False,
                'acc_number': self.group_id.sale_id.acc_number,
                'delivery_instruction': self.group_id.sale_id.delivery_instruction
            })
        return vals
