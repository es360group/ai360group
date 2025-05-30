# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'aigroup360',
    'category': 'Extra Tools',
    'version': '16.0.1',
    'author': '360 Group',
    'website': 'https://360group.ai/',
    'summary': """ AI Tools 360 group""",
    'description': """
        Maximize your productivity and creativity with a suite of advanced tools designed to enhance writing, optimize content, and boost online visibility. Experience innovation that transforms your professional and personal success.
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
