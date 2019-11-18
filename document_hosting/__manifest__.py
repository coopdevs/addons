
# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Document Hosting',

    'summary': """
    Manage the documents of your cooperative.
    """,
    'description': """
    """,

    'author': 'Rémy Taymans',
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': "https://github.com/coopiteasy/addons",

    'category': 'Cooperative Management',

    'depends': [
        'base',
        'web',
        'mail',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/document_hosting_menu.xml',
        'views/document_hosting_views.xml',
    ]
}
