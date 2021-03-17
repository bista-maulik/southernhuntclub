# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def default_get(self, field_list):
        res = super(ResPartner, self).default_get(field_list)
        if self.env.company:
            res['company_id'] = self.env.company.id
        return res
