# -*- coding: utf-8 -*-
# Part of SIMI Technologies
# See LICENSE file for full copyright & licensing details.
# Author: SIMI Technologies
# mail:   solutions@simitechnologies.co.ke
# Copyright (C) 2019-Present SIMI Technologies
# Contributions:
#           SIMI Technologies:
#              - Jessy Ledama

{
    'name': "Custom Excel Reports",
    'author': "SIMI Technologies",
    'website': "http://www.simitechnologies.co.ke",
    'summary': """Print custom excel reports""",
    'description': """This module will print excel report of sale.""",
    'license': 'AGPL-3',
    'category': 'Reports',
    'version': '15.0.1.0.0',
    'depends': [
        'sale_management', 'report_xlsx', 'account'
    ],
    'data': [
        'report/menu_sale_xlsx.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
