# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': "BS Sales",

    'summary': """
        Sales modification""",

    'description': """
        This module contains customization over sales and it's relavent objects.
    """,

    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",

    'category': 'Hidden',
    'version': '1',

    # Dependent module required for this module to be installed
    'depends': ['sale_margin','crm', 'sale_stock', 'bs_product'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_view.xml',
        'views/sales_rep_view.xml',
        'views/res_partner_view.xml',
        'views/sale_view.xml',
        'views/contact_view.xml',
        'report/res_config_settings_views.xml',
        'report/sale_report_view.xml',
        'report/sale_report_templates.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': True
}
