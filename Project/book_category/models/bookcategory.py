# # -*- coding: utf-8 -*-
#
# from odoo import models, fields, api
#
#
# class bookCategory(models.Model):
#     _name = 'book.category'
#     _description = 'Book Category'
#
#     name = fields.Char('Catagory Name', required = True)
#     parent_id = fields.Many2one('book.category', string = 'Parent Category', ondelete = 'cascade', index = True)
#
