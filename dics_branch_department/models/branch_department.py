# -*- coding: utf-8 -*-

import logging
from odoo import models, fields


class BranchDepartment(models.Model):
    _name = "res.branch.department"
    _description = 'Company Branches Departments'

    name = fields.Char(
        'Department',
        required=True,
    )
