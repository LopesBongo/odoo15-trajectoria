from odoo import models, fields


class ProductTemplate(models.Model): # Aqui  não cria um modelo novo, mas modifica o modelo existente product.template do Odoo.
    _inherit = 'product.template' # permite adicionar novos campos ou funções sem mexer no código original do Odoo.

    volume = fields.Float(string="Volume")
    codsup = fields.Char(string="CODSUP")
    format = fields.Selection([
        ('toyota', 'Toyota'),
        ('nissan', 'Nissan'),
        ('honda', 'Honda'),
        ('mercedes', 'Mercedes'),
        ('bmw', 'BMW'),
        ('outro', 'Outro'),
    ], string="Formato/Marca", default="outro")

