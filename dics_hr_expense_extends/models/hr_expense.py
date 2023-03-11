# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Expense(models.Model):
    _inherit = 'hr.expense'

    approved_amount = fields.Float(
        'Approved',
    )
    rejected_amount = fields.Float(
        'Rejected'
    )
    voucher_number = fields.Char(
        'Voucher Number',
        related='sheet_id.voucher_number',
    )

#    @api.model_create_multi
#    def create(self, vals_list):
#        for vals in vals_list:
#            if not vals.get('attachment_number') or  vals.get('attachment_number') <= 0:
#                raise UserError(_("Sorry Attachment should be mendatory"))
#        return super(Expense, self).create(vals_list)
