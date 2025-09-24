from odoo import models, fields

class IESFaculdade(models.Model):
    _name = "ies.faculdade"
    _description = "Faculdade"

    name = fields.Char("Nome da Faculdade", required=True)
    ies_id = fields.Many2one("ies.instituicao", string="Instituição", required=True)
    curso_ids = fields.One2many("ies.curso", "faculdade_id", string="Cursos")
