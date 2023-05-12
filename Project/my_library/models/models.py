# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class my_library(models.Model):
    _name = 'my.library'
    _description = 'my library'

    name = fields.Text('Book Title', required = True)
    short_name = fields.Char('Short Name')
    date_release = fields.Date('Release Date')
    notes = fields.Text('Internal Notes')
    state = fields.Selection([
        ('draft', 'Not Available'),
        ('available', 'Available'),
        ('lost', 'Lost')
    ], string = 'state')
    description = fields.Html(string='Description')
    cover = fields.Binary('Cover')
    out_of_print = fields.Boolean(string='OOP', default=True)
    date_updated = fields.Datetime(string='Date Updated')
    pages = fields.Integer(string='Page')
    reader_rating = fields.Float(string='Reader Average Rating', digits=(10,4))
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary(string="Retail Price")
    author_ids = fields.Many2many('res.partner', string= 'Authors')
    # publisher_id = fields.Many2one('res.partner', string = "Publisher")


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
