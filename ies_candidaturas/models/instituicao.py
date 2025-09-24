from odoo import models, fields

class IESInstituicao(models.Model):
    _name = "ies.instituicao"
    _description = "Instituição de Ensino Superior"

    name = fields.Char("Nome da IES", required=True)
    sigla = fields.Char("Sigla")
    faculdade_ids = fields.One2many("ies.faculdade", "ies_id", string="Faculdades")
