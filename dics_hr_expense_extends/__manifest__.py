# -*- coding: utf-8 -*-

{
    'name': 'Dics HR Expense Extends',
    'version': '16.0.0',
    'summary': "Dics HR Expense Extends",
    'description': """
        Dics HR Expense Extends
    """,
    'author': 'DataInteger Consultancy Services LLP',
    'maintainer':  'DataInteger Consultancy Services LLP',
    'company':  'DataInteger Consultancy Services LLP',
    'website': 'https://www.datainteger.com',
    'category' : "Human Resources/Expenses",
    'depends': [
        'hr_expense',
        'dics_branch_department',
        'multi_branch_base',
    ],
    'data': [
        'data/ir_sequence_data.xml',
        'views/expense_view.xml',
        'views/expense_sheet_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}
