# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ExpenseSheet(models.Model):
    _inherit = 'hr.expense.sheet'

    voucher_number = fields.Char(
        'Voucher Number',
        default=lambda self: _('New'),
        required=True, copy=False, readonly=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'company_id' in vals:
                self = self.with_company(vals['company_id'])
            if vals.get('voucher_number', _("New")) == _("New"):
                seq_date = fields.Datetime.context_timestamp(
                    self, fields.Datetime.to_datetime(vals['date_order'])
                ) if 'date_order' in vals else None
                vals['voucher_number'] = self.env['ir.sequence'].next_by_code(
                    'dics.hr.expense.sheet', sequence_date=seq_date) or _("New")
        return super().create(vals_list)
