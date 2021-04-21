# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, api
from odoo.exceptions import Warning


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_shipping_id')
    def _onchange_partner_shipping_id(self):
        """
        Override the function to stop the warning and set custom warning based
        on requirement.
        :return:
        """
        pickings = self.picking_ids.filtered(lambda p: p.state in ['done', 'cancel'] and p.partner_id != self.partner_shipping_id)
        if pickings:
            raise Warning(
                "You cannot change the address of the delivery order: %s" % (','.join(pickings.mapped('name'))))

    def write(self, vals):
        """
        Override the function to update delivery order delivery address when
        changed in sale order delivery address.
        :param vals:
        :return:
        """
        for rec in self:
            if vals.get('partner_shipping_id', False) and rec.picking_ids:
                picking_ids = rec.picking_ids.filtered(lambda l: l.state not in ['done', 'cancel'])
                if picking_ids:
                    picking_ids.write({'partner_id': vals['partner_shipping_id']})
        return super(SaleOrder, self).write(vals)
