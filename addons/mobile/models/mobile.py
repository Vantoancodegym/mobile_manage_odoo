# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
from odoo import api, fields, models, tools, _
# noinspection PyUnresolvedReferences
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "mobile"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "mobile model"

    name = fields.Char('Mobile Name', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='state', default='draft', clickable=True)
    description = fields.Text('Mobile Description', default= 'Beautiful mobile')
    base_price = fields.Integer('Base Price', default=1000)
    quantity = fields.Integer('Quantity', default=100)
    weight = fields.Float('Weight (g)')
    mfg = fields.Date('Manufacturing Date', required=False)
    color = fields.Selection([
        ('blue', 'Blue'),
        ('white', 'White'),
        ('black', 'Black'),
        ('green', 'Green'),
        ('red', 'Red'),
        ('pink', 'Pink'),
        ('gray', 'Gray')
    ], string='Color', default='blue')
    brand = fields.Selection([
        ('apple', 'Apple'),
        ('samsung', 'Samsung'),
        ('oppo', 'Oppo'),
        ('xiaomi', 'Xiaomi'),
        ('vsmart', 'Vsmart'),
        ('huawei', 'Huawei'),
        ('sony', 'Sony'),
    ], string='Color', default='blue')
    mobile_image = fields.Binary("Mobile Image", attachment=True, help="Pet Image")

    total = fields.Float(compute='_compute_total')

    @api.depends('base_price', 'quantity')
    def _compute_total(self):
        for record in self:
            record.total = record.base_price * record.quantity

    @api.constrains("base_price")
    def check_age(self):
        for record in self:
            if record.base_price <= 0:
                raise ValidationError("base_price must lager than 0")

    @api.constrains("quantity")
    def check_age(self):
        for record in self:
            if record.base_price <= 0:
                raise ValidationError("quantity must lager than 0")