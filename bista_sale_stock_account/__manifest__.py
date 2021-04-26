# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

{
    'name': "Bista Sale Stock Account",
    'category': 'Sale/Inventory',
    'summary': "Sale Stock Account Customization",
    'description': """
Sale Stock Account Customization,
===================================================================
    *This module is used to customization sale stock and account to pass the 
    details from sale order to delivery and then invoice.
    """,
    'version': '14.0.1.0.0',
    'author': 'Bista Solutions Pvt. Ltd.',
    'website': 'https://www.bistasolutions.com',
    'company': 'Bista Solutions Pvt. Ltd.',
    'maintainer': 'Bista Solutions Pvt. Ltd',
    'depends': ['bs_inventory_transfer', 'bs_account'],
    'data': [
        'security/ir.model.access.csv',
        'views/preferred_carrier_view.xml',
        'views/sale_view.xml',
        'views/stock_picking_view.xml',
        'views/account_move_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
