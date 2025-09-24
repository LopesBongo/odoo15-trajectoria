from odoo import models, fields

class Doctor(models.Model): # Cria uma classe Python chamada Doctor.
    _name = 'hospital.doctor'  # será o nome do modelo usado internamente pelo Odoo
    _description = 'Doctor'

    # Campos que todo Doctor tera
    name = fields.Char("Nome", default=True)
    speciality = fields.Char(string='Especialidade médica')
    phone = fields.Char(string='Telefone')
    email = fields.Char(string='Email')
    active = fields.Boolean(string='Ativo', default=True)

