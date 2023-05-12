# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EducationStudent(models.Model):
    _name = 'education.student'

    state = fields.Selection(string='Status', selection=[('new', 'New'),
                                                         ('studying', 'Studying'),
                                                         ('off', 'Off')], default='new')

    @api.model
    def is_allowed_state(self, current_state, new_state):
        allowed_states = [('new', 'studying'), ('studying', 'off'), ('off', 'studying'), ('new', 'off')]
        return (current_state, new_state) in allowed_states

    def change_student_state(self, state):
        for student in self:
            if student.is_allowed_state(student.state, state):
                student.state = state
            else:
                continue

    def change_to_new(self):
        self.change_student_state('new')

    def change_to_studying(self):
        self.change_student_state('studying')

    def change_to_off(self):
        self.change_student_state('off')
