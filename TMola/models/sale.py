from xlwt.ExcelFormulaLexer import false_pattern

from odoo import models, fields


class SaleOrder(models.Model): #  Modifico o modelo existente sale.order do Odoo.
    _inherit = 'sale.order'  # permite adicionar novos campos sem mexer no código original.

    vehicle_model = fields.Char(string="Modelo/Marca")
    vehicle_plate = fields.Char(string="Matrícula")
    vehicle_color = fields.Char(string="Cor")
    vehicle_km = fields.Integer(string="KM")
    vehicle_chassis = fields.Char(string="Nº do Chassi")


