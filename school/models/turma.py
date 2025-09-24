from odoo import models, fields

class SchoolClass(models.Model):
    _name = "school.class"
    _description = "Turma"

    name = fields.Char(string="Nome da Turma", required=True)
    teacher_id = fields.Many2one("school.teacher", string="Professor")
    student_ids = fields.One2many("school.student", "class_id", string="Alunos")
