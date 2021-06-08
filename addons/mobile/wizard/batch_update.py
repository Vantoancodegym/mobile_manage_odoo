# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
from odoo import api, fields, models, tools, _
# noinspection PyUnresolvedReferences
from odoo.exceptions import UserError, ValidationError

import logging

_logger = logging.getLogger(__name__)


class BatchUpdateWizard(models.TransientModel):
    _name = "mobile.batchupdate.wizard"
    _description = "Batch update for mobile model"

    mfg = fields.Date('Manufacturing Date', required=False, default=False)
    quantity = fields.Integer('Quantity', required=False, default=False)
    weight = fields.Float('Weight (g)', required=False, default=False)

    def multi_update(self):
        ids = self.env.context['active_ids']  # selected record ids
        mobiles = self.env["mobile"].browse(ids)
        new_data = {}

        if self.mfg:
            new_data["mfg"] = self.mfg
        if self.quantity:
            new_data["quantity"] = self.quantity
        if self.weight:
            new_data["weight"] = self.weight

        mobiles.write(new_data)