# -*- coding: utf-8 -*-

{
    'name': 'Dics Branch Department',
    'version': '16.1.0',
    'summary': "Branch Departments",
    'description': """
        Add Departments for the branches
    """,
    'author': 'DataInteger Consultancy Services LLP',
    'maintainer':  'DataInteger Consultancy Services LLP',
    'company':  'DataInteger Consultancy Services LLP',
    'website': 'https://www.datainteger.com',
    'category' : "Tools",
    'depends': [
        'multi_branch_base',
        'purchase',
        'hr_expense',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/branch_view.xml',
        'views/res_branch__department_views.xml',
        'views/purchase_view.xml',
        'views/expense_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}
