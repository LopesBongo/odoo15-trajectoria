from odoo import models, fields, api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval_date = fields.Datetime(string='Data de Aprovação', readonly=True)

    @api.model
    def _get_current_datetime(self):
        return fields.Datetime.now()

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            order.approval_date = self._get_current_datetime()
        return res
