from odoo import models, api


class ReportVehicleMovement(models.AbstractModel):
    _name = 'tmola.report_vehicle_movement_document'
    _description = 'Relatório de Movimentações de Veículos'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Pega todas as movimentações
        docs = self.env['vehicle.movement'].search([], order='entry_date asc')
        return {
            'doc_ids': docs.ids,
            'doc_model': 'vehicle.movement',
            'docs': docs,
        }
