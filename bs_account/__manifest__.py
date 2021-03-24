# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': "BS Account",

    'summary': """
        Account modification""",

    'description': """
        This module contains customization over sales and it's relavent objects.
    """,

    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",

    'category': 'Hidden',
    'version': '1',

    # Dependent module required for this module to be installed
    'depends': ['bs_sales'],
    # always loaded
    'data': [
        'views/account_move_view.xml',
        'report/report_invoice_template.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': True
}