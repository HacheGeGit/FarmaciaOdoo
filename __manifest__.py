# -*- coding: utf-8 -*-
{
    'name': "farmacia",

    'summary':  """
                Módulo que permite la gestión de los productos de una farmacia, así como de sus recetas.
                """,

    'description':  """
                    Descripción.    
                    """,

    'author': "Hugo González Sánchez",
    'website': "http://www.iesvenancioblanco.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/grupos.xml',
 	    'security/ir.model.access.csv',
        'views/views.xml',
        'views/vistas2.xml',
        #'reports/informes.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'instalation': True,
    'application': True
}
