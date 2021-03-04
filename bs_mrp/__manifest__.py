# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': "BS Manufacturing",

    'summary': """
        Manufacturing modification""",

    'description': """
        This module contains customization over Manufacturing and it's relavent objects.
    """,

    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",

    'category': 'Hidden',
    'version': '1',

    # Dependent module required for this module to be installed
    'depends': ['mrp','mrp_workorder'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_view.xml',
        'views/storage_type_view.xml',
        'views/product_view.xml',
        'views/mrp_bom_view.xml',
        'views/mrp_production_view.xml',
        'report/mrp_production_templates.xml',
        'views/mrp_workorder_view.xml',
    ],
    'images': ['static/description/icon.png'],
    
    'installable': True,
    'auto_install': False,
    'application': True
}
