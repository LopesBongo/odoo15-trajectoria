from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    client_number = fields.Char(
        string="Número do Cliente",
        readonly=True,  # o usuário não consegue alterar manualmente
        copy=False,  # não é copiado em duplicações
        default=lambda self: "New",  # valor padrão para novos clientes
        index=True  # facilita buscas no banco
    )

    @api.model
    def create(self, vals):
        # só gera número se ainda estiver como "New"
        if vals.get('client_number', 'New') == 'New':
            vals['client_number'] = self.env['ir.sequence'].next_by_code(
                'res.partner.sequence'
            ) or '/'
        return super(ResPartner, self).create(vals)
