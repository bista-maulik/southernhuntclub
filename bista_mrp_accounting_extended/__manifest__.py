# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'MRP Accounting Extended',
    "version": "14.0.0.1",
    'category': 'Accounting',
    'author': 'Bista Solutions Pvt. Ltd.',
    "website": "http://www.bistasolutions.com",
    'depends': ['base', 'mrp', 'stock_account'],
    'description': """ 
MRP Accounting Extended
=============================
This module sets MRP Stock Input and MRP Stock Output Accounts which are configured in the Product Categories into Journal Entries
for Manufacturing Orders.
    """,
    'data': ['views/product_category_view.xml',
    'views/mrp_production.xml'],
    'installable': True,
    'auto_install': False,
}
