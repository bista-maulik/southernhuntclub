# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': "BS Product",

    'summary': """
        Product modification""",

    'description': """
        This module contains customization over Product and it's relavent objects.
    """,

    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",

    'category': 'Hidden',
    'version': '1',

    # Dependent module required for this module to be installed
    'depends': ['base','product'],
    # always loaded
    'data': [
        'views/product_template_view.xml',
        ],

    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': True
}
