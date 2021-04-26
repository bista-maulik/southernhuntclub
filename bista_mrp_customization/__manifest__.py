# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

{
    'name': "Bista Manufacturing Customization",
    'category': 'Manufacturing',
    'summary': "Manufacturing Customization",
    'description': """
Manufacturing Customization,
===================================================================
    *This module is used to customization manufacturing order and related 
    backorder.
    """,
    'version': '14.0.1.0.0',
    'author': 'Bista Solutions Pvt. Ltd.',
    'website': 'https://www.bistasolutions.com',
    'company': 'Bista Solutions Pvt. Ltd.',
    'maintainer': 'Bista Solutions Pvt. Ltd',
    'depends': ['bs_mrp'],
    'data': [
        'views/mrp_production_view.xml',
        'views/res_config_settings_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
