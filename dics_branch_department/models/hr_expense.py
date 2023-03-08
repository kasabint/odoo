# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Expense(models.Model):
    _inherit = 'hr.expense'

    allowed_branch_ids = fields.Many2many('res.branch', store=True,
                                          string="Allowed Branches",
                                          compute='_compute_allowed_branch_ids')

    branch_id = fields.Many2one("res.branch", string='Branch', store=True,
                                readonly=False,
                                compute="_compute_branch")

    branch_department_ids = fields.Many2many(
        'res.branch.department',
        compute='_compute_branch_department_ids',
        string='Branch Departments',
    )
    branch_department_id = fields.Many2one(
        "res.branch.department",
        string='Department',
        store=True,
        readonly=False,
    )


    @api.depends('company_id')
    def _compute_allowed_branch_ids(self):
        for po in self:
            po.allowed_branch_ids = self.env.user.branch_ids.ids

    @api.depends('company_id')
    def _compute_branch(self):
        for expense in self:
            company = self.env.company
            so_company = expense.company_id if expense.company_id else self.env.company
            branch_ids = self.env.user.branch_ids
            branch = branch_ids.filtered(
                lambda branch: branch.company_id == so_company)
            if branch:
                expense.branch_id = branch.ids[0]
            else:
                expense.branch_id = False

    @api.depends('branch_id')
    def _compute_branch_department_ids(self):
        for rec in self:
            rec.branch_department_ids = rec.branch_id.branch_department_ids
    
    def _get_default_expense_sheet_values(self):
        branch_ids = self.mapped('branch_id')
        branch_department_ids = self.mapped('branch_department_id')
        if len(branch_ids) > 1 or len(branch_department_ids) > 1:
            raise UserError(_("Branch or Department is not same on selected expenses"))
        values = super(Expense, self)._get_default_expense_sheet_values()
        for vals in values:
            vals.update({
                'branch_id': self[0].branch_id.id,
                'branch_department_id': self[0].branch_department_id.id,
            })
        return values

