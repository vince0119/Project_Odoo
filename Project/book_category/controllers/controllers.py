# -*- coding: utf-8 -*-
# from odoo import http


# class BookCategory(http.Controller):
#     @http.route('/book_category/book_category/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/book_category/book_category/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('book_category.listing', {
#             'root': '/book_category/book_category',
#             'objects': http.request.env['book_category.book_category'].search([]),
#         })

#     @http.route('/book_category/book_category/objects/<model("book_category.book_category"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('book_category.object', {
#             'object': obj
#         })
