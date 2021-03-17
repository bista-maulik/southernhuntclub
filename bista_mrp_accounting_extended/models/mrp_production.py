# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'

    def show_journal_entries(self):
        """
        Define the function which shows you the journal entries which created
        when the current production done.
        :return:
        """
        for each in self:
            # cr = each._cr
            # each_id = each.id
            tree_view_id = self.env.ref('account.view_move_tree').id
            form_view_id = self.env.ref('account.view_move_form').id
            # cr.execute("""select am.id from account_move am
            #             left join stock_move mv on mv.id = am.stock_move_id
            #             where mv.production_id= %s or mv.raw_material_production_id = %s""" % (each_id, each_id))
            domain = each.get_journal_entry_domain()
            account_move_ids = self.env['account.move'].search(domain)
            # account_move_ids = list(filter(None, map(lambda x: x[0], cr.fetchall())))
            if account_move_ids:
                return {
                    'name': _('Journal Entries'),
                    'type': 'ir.actions.act_window',
                    'res_model': 'account.move',
                    'view_type': 'form',
                    'view_mode': 'tree,form',
                    'target': 'current',
                    'context': self._context,
                    'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
                    'domain': [('id', 'in', account_move_ids.ids)]
                }
            else:
                raise UserError(_("No Journal Entries Found."))

    def get_journal_entry_domain(self):
        """
        Define function to return the domain for journal entry.
        :return:
        """
        domain = [
            '|', ('stock_move_id.production_id', '=', self.id),
            ('stock_move_id.raw_material_production_id', '=', self.id)]

        return domain
