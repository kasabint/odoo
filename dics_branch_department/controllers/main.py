# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class ScanPistol(http.Controller):
    @http.route([
        '''/scan/pistol/picking''',
    ], type='http', auth="user", website=True)
    def ScanPistol(self, **post):
        return request.render("dics_web_pistol_scan_picking.scan_pistol_web_tmpl", {})
    
    @http.route(['/scan/pistol/redirect'], type='json', auth="user", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, picking_number=None):
        stock_picking_id = request.env['stock.picking'].search([
            ('name', '=', picking_number)
        ])
        if stock_picking_id.move_ids_without_package and stock_picking_id.move_ids_without_package[0].move_dest_ids:
            move_dest_id = stock_picking_id.move_ids_without_package[0].move_dest_ids.filtered(lambda move_dest:move_dest.state == 'assigned')
            if move_dest_id:
                move_dest_id = move_dest_id[0]
                picking_id = request.env['stock.picking'].search([
                    ('name', '=', move_dest_id.reference),
                ])
                stock_picking_id = picking_id
        url = False
        if stock_picking_id:
            action_id = request.env.ref('stock.action_picking_tree_all').id
            url = "/web#return_label=Website&model=%s&id=%s&;action=%s&;view_type=form" % ('stock.picking', str(stock_picking_id.id), str(action_id))
        return {
            'url': url if url else False,
        }
