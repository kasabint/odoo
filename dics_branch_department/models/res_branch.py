# -*- coding: utf-8 -*-

import logging
from odoo import models, fields


class Branch(models.Model):
    _inherit = "res.branch"
    _description = 'Company Branches Departments'

    branch_department_ids = fields.Many2many(
        'res.branch.department',
        string='Departments'
    )
