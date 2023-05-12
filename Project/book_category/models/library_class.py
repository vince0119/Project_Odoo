# from odoo import fields, models, api
# from odoo.exceptions import UserError
#
# class library_class(models.Model):
#     _name = 'library.class'
#
#     library_ids = fields.One2many('my.library', 'class_id', string='library')
#
#     def get_all_library(self):
#         # Khởi tạo đối tượng my.library (đây là một recordset rỗng của model my.library)
#         library = self.env['my.library']
#         all_library = library.search([])
#         print("All Library: ", all_library)