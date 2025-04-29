# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'aigroup360',
    'category': 'Extra Tools',
    'version': '16.0.1',
    'author': '360 Group',
    'website': 'https://360group.es/',
    'summary': """Herramientas IA 360 group""",
    'description': """
        Este modulo da acceso a varias herramientas que ofrece 360 group,
        teniendo opciones gratuitas y de pago
    """,
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/dynamic_iframe_view.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.gif'],
    'application': True,
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'ai360group/static/src/js/webiframe.js',
            'ai360group/static/src/css/style.css',
        ],
    },
    'price': 50,
    'currency': 'EUR',
}
