# -*- coding: utf-8 -*-
{
    'name': 'Pricelist Update Wizard',
    'version': '1.0',
    'summary': 'Bulk update product sales and cost prices using a wizard.',
    'sequence': 10,
    'description': """
Product Price Update Wizard
===========================
This module adds an action in the product list view allowing users 
to select multiple products and update their prices (sale price or cost) 
by a percentage or a fixed amount in bulk.
    """,
    'category': 'Sales/Sales',
    'author': 'Sven Wehrend',
    'website': 'https://github.com/wehrend/product_price_update_wizard',
    'depends': [
        'base',
        'product',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/pricelist_update_wizard_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}