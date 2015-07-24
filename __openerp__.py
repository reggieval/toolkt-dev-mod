{
    'name': 'Toolkt Custom Forms',
    'category': 'Specific Industry Applications',
    'summary': 'A module that contains customizations for Toolkt Inc.',
    'version': '0.1',
    'description': """


Toolkt, Inc.
====================================
Toolkt Inc. Customizations



        """,
    'author': 'Toolkit',
    'depends': [
        'base', 'l10n_ph', 'product', 'purchase_requisition', 'hr', 'sale', 'purchase', 'pentaho_reports', 'stock'

    ],
    'demo': [
    ],
    'data': [

        'employee_profile_view.xml',
        'visitors_view.xml',

    ],
    'qweb': [

    ],
    'installable': True,
}
