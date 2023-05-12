# from odoo import models, fields, api, _
#
# class LibraryBook(models.Model):
#     _name = 'library.book'
#     _description = 'Library Book'
#
#     # name = fields.Char(string='Name', required=True,
#     # help='Enter the name of the book.')
#     #
#     # _sql_constraints = [('name_uniq', 'unique(name)', 'The book name must be unique!'),]
#     # age_days = fields.Integer(string = 'Age(days)', compute = '_compute_age_days', store = True)
#     # "compute='_compute_age_days'" chỉ định hàm tính toán giá trị cho trường "age_days".
#     # "store=True" đảm bảo dữ liệu của trường sẽ được lưu trữ trên cơ sở dữ liệu.
#
#     # name = fields.Char('Title')
#     # author = fields.Many2one('res.partner', string='Author')
#     # publisher = fields.Many2one('res.partner', string='Publisher')
#     # state_available = fields.Boolean('Available', default=True)
#     # state_borrowed = fields.Boolean('Borrowed')
#     # state_lost = fields.Boolean('Lost')
#     # my_library_ids = fields.One2many('my.library', 'book_id', string = 'My Library')
#
#     @api.multi
#     def action_make_available(self):
#         self.state_available = True
#         self.state_borrowed = False
#         self.state_lost = False
#         for record in self.my_library_ids:
#             return record_book()
#
#     @api.multi
#     def action_make_borrowed(self):
#         self.state_available = False
#         self.state_borrowed = True
#         self.state_lost = False
#         self.my_library_ids.create({'book_id': self.id, 'state_borrowed':True})
#
#     @api.multi
#     def action_make_lost(self):
#         self.state_available = False
#         self.state_borrowed = False
#         self.state_lost = True
#         for record in self.my_library_ids:
#             record.return_book()
