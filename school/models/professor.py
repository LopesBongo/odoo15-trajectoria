from odoo import models, fields

class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "Professor"

    name = fields.Char(string="Nome", required=True)
    subject = fields.Char(string="Disciplina")
    class_ids = fields.One2many("school.class", "teacher_id", string="Turmas")
