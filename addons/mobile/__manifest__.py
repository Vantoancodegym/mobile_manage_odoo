# -*- coding: utf-8 -*-
{
    'name': "Mobile manage",
    'summary': """Mobile manage""",
    'description': """Mobile manage""",
    'author': "vantoanftu93@gmail.com",
    'website': "vantoanftu93@gmail.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'views/mobile.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}