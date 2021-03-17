# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def default_get(self, field_list):
        """
        Override function to set default company in product.
        :param field_list:
        :return:
        """
        res = super(ProductTemplate, self).default_get(field_list)
        if self.env.company:
            res['company_id'] = self.env.company.id
        return res
