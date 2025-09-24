from odoo import models, fields


class Student(models.Model):
    _name = 'school.student'  # nome técnico da tabela
    _description = 'Aluno'  # descrição do modelo

    name = fields.Char(string='Nome', required=True)
    birth_date = fields.Date(string='Data de Nascimento', required=True)
    gender = fields.Selection([
        ("male", "Masculino"),
        ("female", "Feminina"),
        ("others", "Outro")
    ], string='Genero', default='male', required=True)  # lista de opções (Masculino/Feminino/outros).
    class_id =  fields.Many2one('school.class', string='Turma') #cria um relacionamento com outro modelo chamado Turma