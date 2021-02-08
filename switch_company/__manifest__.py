# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2020 (http://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'BS Switch Company',
    'version': '1',
    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",
    'category': 'Hidden',
    'summary': 'Switch Company',
    'description': """Select only one company at a time
""",

    # Dependent module required for this module to be installed
    'depends': ['web'],
    
    #Always loaded
    'data': [
        'views/template.xml',
        ],
  
    'installable': True,
    'auto_install': False,
}
