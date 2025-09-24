from odoo import models, fields, api #importa as classes base do Odoo



class Appointment(models.Model):  # Define um modelo Odoo.
    _name = 'medical.appointment'  # será o nome do modelo usado internamente pelo Odoo
    _description = 'Atendimento Médico'

    _rec_name ='patient_id'

    # Relacionamento com o paciente
    patient_id = fields.Many2one(
        comodel_name='medical.patient',
        string='Paciente',
        required=True
    )
    # Many2one cria a ligação de cada médico a um paciente

    # Relacionamento com o médico
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Médico',
        required=True
    )
    # Many2one cria a ligação de cada Hospital a um Doctor

    # Data da consulta
    appointment_date = fields.Date(
        string='Data da Consulta',
        required=True
    )

    # Descrição da consulta
    description = fields.Text(
        string='Detalhes da Consulta'
    )

    # Estado da consulta
    state = fields.Selection(
        selection=[
            ('draft', 'Rascunho'),
            ('confirmed', 'Confirmada'),
            ('done', 'Concluída'),
            ('cancelled', 'Cancelada')
        ],
        string='Estado',
        default='draft',
        required=True
    )
