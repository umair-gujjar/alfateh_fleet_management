# -*- coding: utf-8 -*-
{
    'name': "Alfateh Fleet Management",

    'summary': """
        Purpose of this module is to manage Trip Management and Cost
        of different Routes. It also include Schedule Management, Card Management, 
        Logs and Reporting """,

    'description': """
        
    """,

    'author': "OxenLab",
    'website': "http://www.oxenlab.com",
    'category': 'aaps',
    'version': '0.1',
    'depends': ['base','fleet'],
    'data': [
        # 'security/ir.model.access.csv',
        #'templates.xml',
        'vechicle_view.xml',
        'route_management_view.xml',
        'trip_management_view.xml',
        'fuel_card_management_view.xml',
    ],
}
