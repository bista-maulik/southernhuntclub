# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'Bista MRP Labour Cost',
    'version': "14.0.0.1",
    'author': 'Bista Solutions Pvt. Ltd.',
    'website': "http://www.bistasolutions.com",
    'category': 'MRP',
    'summary': "Creates the Journal entry for individul workorder cost with corresponding employee",
    'description': """
        Creates the Journal entry for individul workorder cost with corresponding employee
    """,
    'depends': ['bista_mrp_accounting_extended'],
    'data': [
            'views/mrp_workcenter_view.xml'
    ],
    'installable': True,
    'auto_install': True
}
