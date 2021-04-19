# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': "BS Inventory Transfer(Stock)",

    'summary': """
        stock related modification""",

    'description': """
        This module contains customization over Stock and it's relavent objects.
    """,

    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",

    'category': 'Hidden',
    'version': '1',

    # Dependent module required for this module to be installed
    'depends': ['bs_sales'],
    # always loaded
    'data': [
        'security/security_view.xml',
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/stock_picking_view.xml',
        'report/report_templates.xml',
        'report/pending_delivery_order_view.xml',
        'report/report_delivery_slip.xml',
        # 'views/res_config_settings_view.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': True
}
