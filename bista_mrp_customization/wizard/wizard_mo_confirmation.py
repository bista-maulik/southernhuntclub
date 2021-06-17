# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields


class WizardMoConfirmation(models.TransientModel):
    _name = "wizard.mo.confirmation"
    _description = " Wizard Manufacturing Confirmation"

    name = fields.Char(
        string="Name",
        default="The Transfer is not processed, Are you sure you want to Mark as Done Manufacturing order without the Transfer process?")
    production_id = fields.Many2one('mrp.production',
                                    string="Manufacturing Order")

    def confirm_mo(self):
        """
        Define function that process the manufacturing order after the
        confirmation.
        :return:
        """
        if self.production_id:
            context = self._context.copy()
            context.update({'confirmation': True})
            res = self.production_id.with_context(context).button_mark_done()
            return res
        else:
            return True
