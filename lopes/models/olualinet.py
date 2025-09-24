from odoo import models, fields

class Olualinet(models.Model):

    _name = 'olualinet.training' #Nome do objecto(equivalente a olualinet_training na bd do postgreSQL)
    _description = 'Treinamento na Olualinet'

    name = fields.Char("Name")
    category = fields.Char(string="Category")
    passport_number = fields.Integer(str='Numero de passaporte')
    balance_number = fields.Float(str='Saldo')
    ative = fields.Boolean(str='Ativo', default=True)
    gender = fields.Selection([("male", "Masculino"), ("female", "Famenino"), ("others", "Outro")], str="Genero" , default="male")
    today_date = fields.Date(str='report')

