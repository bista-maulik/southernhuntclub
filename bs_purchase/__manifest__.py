# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': "BS Purchase",

    'summary': """
        Purchase modification""",

    'description': """
        This module contains customization over purchase and it's relavent objects.
    """,

    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",

    'category': 'Hidden',
    'version': '1',

    # Dependent module required for this module to be installed
    'depends': ['purchase','bs_sales'],
    # always loaded
    'data': [
        'views/purchase_order_view.xml',
        'views/res_partner_view.xml',
        'report/report_purchase_template.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': True
}
