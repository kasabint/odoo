# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons.purchase.models.purchase import PurchaseOrder as Purchase
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

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

    @api.depends('branch_id')
    def _compute_branch_department_ids(self):
        for rec in self:
            rec.branch_department_ids = rec.branch_id.branch_department_ids


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    branch_department_id = fields.Many2one(
        related='order_id.branch_department_id',
        string='Department',
        store=True
    )
