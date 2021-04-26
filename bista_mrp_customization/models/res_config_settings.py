# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    is_transfer_process_validation = fields.Boolean(string="Want To Check Transfer Process Validation",
        config_parameter='bista_mrp_customization.is_transfer_process_validation')
