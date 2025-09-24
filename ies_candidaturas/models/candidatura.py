# models/candidatura.py
from odoo import models, fields

class IESCandidatura(models.Model):
    _name = "ies.candidatura"
    _description = "Candidatura do Candidato"

    candidato_id = fields.Many2one("res.partner", string="Candidato", required=True)
    curso_id = fields.Many2one("ies.curso", string="Curso", required=True)
    estado = fields.Selection([
        ("processando", "Processando"),
        ("aceite", "Aceite"),
        ("rejeitado", "Rejeitado"),
    ], default="processando", string="Estado")
