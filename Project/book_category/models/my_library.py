# from odoo import fields, models, api
# from odoo.exceptions import UserError
#
#
#
# class my_library(models.Model):
#     _name = 'my.library'
#     _description = 'My Library'
#
#     class_id = fields.Many2one('library.class', string='Class', ondelete="restrict")
#     state = fields.Selection(string='Status', selection=[('draft', 'available'),
#                                                          ('available', 'borrowed'),
#                                                          ('borrowed', 'available'),
#                                                          ('available', 'lost'),
#                                                          ('borrowed', 'lost'),
#                                                          ('lost', 'available')], default='draft')
#
#     @api.model
#     def is_allowed_state(self, current_state, new_state):
#         allowed_states = [('draft', 'available'),
#                           ('available', 'borrowed'),
#                           ('borrowed', 'available'),
#                           ('available', 'lost'),
#                           ('borrowed', 'lost'),
#                           ('lost', 'available')]
#         return (current_state, new_state) in allowed_states
#
#     def change_state(self, state):
#         for action in self:
#             if action.is_allowed_state(action.state, state):
#                 action.state = state
#             else:
#                 raise UserError(_("Changing state status from %s to %s is not allowed.") % (action.state, state))
#
#     def action_make_available(self):
#         self.change_state('Make Available')
#
#     def action_make_borrowed(self):
#         self.change_state('Make Borrowed')
#
#     def action_make_lost(self):
#         self.change_state('Make Lost')