# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductPricelistUpdateWizard(models.TransientModel):
    _name = 'product.pricelist.update.wizard'
    _description = 'pricelist_bulk_update'

    # Holt sich die IDs der ausgewählten Preislisten
    pricelist_ids = fields.Many2many(
        'product.pricelist', 
        default=lambda self: self.env.context.get('active_ids')
    )
    
    update_type = fields.Selection([
        ('percent', 'Percentage (%)'),
        ('fixed', 'Fixed Amount (€)')
    ], string="Type of pricelist adaption", default='percent', required=True)

    value = fields.Float(string="Value", required=True)

    def action_apply_pricelist_update(self):
        self.ensure_one()
        
        items = self.env['product.pricelist.item'].search([
            ('pricelist_id', 'in', self.pricelist_ids.ids)
        ])

        for item in items:
            if item.compute_price == 'fixed':
                current_price = item.fixed_price
                
                if self.update_type == 'percent':
                    new_price = current_price * (1 + (self.value / 100.0))
                else:
                    new_price = current_price + self.value
                    
                item.write({'fixed_price': max(0.0, new_price)})
                
            # Advanced: If the price list is based on formulas (e.g. base price - 10%)
            elif item.compute_price == 'formula':
                # Here we change the markup/discount (price_discount) 
                # # Attention: Odoo stores discounts in formulas positively (e.g. 10 for -10%)
                if self.update_type == 'percent':
                    item.price_discount += self.value  # Increases or decreases the discount

        return {'type': 'ir.actions.act_window_close'}