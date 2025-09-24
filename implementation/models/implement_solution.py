from odoo import models, fields

class Solution(models.Model):
    # Uma Classe que mostra a soluçao de um determinado trabalho
    _name = 'implement.solution'
    _description = 'Soluçao'

    # Campos que mostra a soluçao de todos clientes
    name = fields.Char("Nome")
    type = fields.Char(string='Tipo')
    category = fields.Selection([
        ("health", "Saude"),
        ("education", "Educaçao"),
        ("others", "Outro")
    ], string="Categoria" , default="health")
