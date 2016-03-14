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
    'depends': ['base','mail','fleet','stock'],
    'data': [
        # 'security/ir.model.access.csv',
        #'templates.xml',
        'sequence.xml',
        'vechicle_view.xml',
        'route_management_view.xml',
        'fuel_rate_view.xml',
        'trip_management_view.xml',
        'location_view.xml',
        'inwardpass.xml',
        'driver_view.xml',
        'security/inwardpass_security.xml',
        'security/ir.model.access.csv',
        'fuel_card_management_view.xml',
        'checklist_view.xml',
        'wizard/fuelcardwizard_view.xml',
        'branding_merchandise_mangment.xml',
    ],
}
