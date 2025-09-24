from odoo import models, fields, api
from datetime import datetime

class VehicleMovement(models.Model): # Aqui você está criando um modelo novo chamado vehicle.movement.
    _name = 'vehicle.movement'
    _description = 'Movimentação de Veículos'


    name = fields.Char(
        string="Número de Movimentação",
        readonly=True,
        copy=False, required=True,
        default=lambda self: '/' #começa como '/' e será substituído por uma sequência automática no create.

    )
    # Cada movimentação está ligada a uma ordem de venda
    vehicle_id = fields.Many2one('sale.order',
                                 string="Veículo/Ordem de Venda",
                                 required=True
                                 )
    # Campos relacionados ao veículo e cliente
    client_id = fields.Many2one('res.partner',
                                string="Cliente",
                                # para pegar informações diretamente da ordem de venda:
                                related='vehicle_id.partner_id',
                                readonly=True
                                )

    vehicle_model = fields.Char(string="Modelo/Marca",
                                # para pegar informações diretamente da ordem de venda:
                                related='vehicle_id.vehicle_model',
                                readonly=True
                                )

    vehicle_plate = fields.Char(string="Matrícula",
                                # para pegar informações diretamente da ordem de venda:
                                related='vehicle_id.vehicle_plate',
                                readonly=True)

    # automaticamente preenchida com a report atual
    entry_date = fields.Datetime(string="Data de Entrada",
                                 default=fields.Datetime.now,
                                 required=True
                                 )

    exit_date = fields.Datetime(string="Data de Saída")
    notes = fields.Text(string="Observações")

    status = fields.Selection([
        ('entry', 'Entrada'),
        ('in_service', 'Em Serviço'),
        ('exit', 'Saída'),
        ('confirmed', 'Confirmado'),
        ('cancelled', 'Cancelado'),
    ], string="Status", default='entry', required=True)

    # ---- Ações da barra de estado ----
    def action_entry(self):
        for record in self:
            record.status = 'entry'
            record.entry_date = fields.Datetime.now()
            record.exit_date = False

    def action_in_service(self):
        for record in self:
            record.status = 'in_service'

    def action_exit(self):
        for record in self:
            record.status = 'exit'
            record.exit_date = fields.Datetime.now()

    # ---- Ações dos botões ----
    def action_confirm_email(self):
        for record in self:
            record.status = 'confirmed'
            # aqui pode integrar envio de email
        return True

    def action_confirm(self):
        for record in self:
            record.status = 'confirmed'
        return True

    def action_cancel(self):
        for record in self:
            record.status = 'cancelled'
        return True


    @api.model
    def create(self, vals):
        # Gerar números sequencial automático
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('vehicle.movement.sequence') or '/'
        return super(VehicleMovement, self).create(vals)



