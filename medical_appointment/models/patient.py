from odoo import models, fields


class MedicalPatient(models.Model):
    _name = 'medical.patient'  # Nome do objecto(equivalente a olualinet_training na bd do postgreSQL)
    _description = 'pacient'

    # Campos que todo paciente tera
    name = fields.Char("Nome", required=True)
    birth_date = fields.Date(string='Data de Nascimento', required=True)
    phone = fields.Char(string='Telephone', required=True)
    email = fields.Char(string='Email')
    address = fields.Text(string='Endereço', required=True)
    gender = fields.Selection([
        ("male", "Masculino"),
        ("female", "Feminino"),
        ("others", "Outro")
    ], string="Gênero", default="male", required=True)

