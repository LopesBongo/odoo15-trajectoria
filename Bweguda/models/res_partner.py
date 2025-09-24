from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_code = fields.Char(
        string='Código Interno do Cliente',
        readonly=True,
        copy=False
    )

    @api.model
    def create(self, vals):
        # só gera número se ainda estiver como "New"
        if vals.get('customer_code', 'New') == 'New':
            vals['customer_code'] = self.env['ir.sequence'].next_by_code(
                'res.partner.sequence'
            ) or '/'
        return super(ResPartner, self).create(vals)
