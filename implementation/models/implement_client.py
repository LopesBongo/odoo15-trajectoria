from odoo import models, fields

class Clients(models.Model):
    _name = 'implement.client' #Nome do objecto(equivalente a olualinet_training na bd do postgreSQL)
    _description = 'Cliente'

    # Campos que todo cliente tera
    name = fields.Char('Nome')
    tel = fields.Char(string='Telephone')
    email = fields.Char(string='Email')
    nif = fields.Char(string='NIF')
    code = fields.Integer(string='Code', required=True, copy=False)

    _sql_constraints = [
        ('unique_code', 'unique(code)', 'O código deve ser único!')
    ]
