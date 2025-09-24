# models/curso.py
from odoo import models, fields

class IESCurso(models.Model):
    _name = "ies.curso"
    _description = "Curso"

    name = fields.Char("Nome do Curso", required=True)
    faculdade_id = fields.Many2one("ies.faculdade", string="Faculdade", required=True)
    candidatura_ids = fields.One2many("ies.candidatura", "curso_id", string="Candidaturas")
