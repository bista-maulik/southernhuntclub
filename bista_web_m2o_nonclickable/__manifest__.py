# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'Bista Disable Create Master Data',
    'version': '14.0.1.0.0',
    'category': 'Hidden/Tools',
    'description': """
    This module remove the create functionality of master data on the fly.
    """,
    'author': 'Bista Solutions Pvt.Ltd.',
    'website': 'https://www.bistasolutions.com/',
    'depends': ['web'],
    'data': [
        'security/security.xml',
        'views/templates.xml',
    ],
    'installable': True,
}
