from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "Project.study"
    _description = "Project Study"

    name = fields.Char('Book Title', required=True)
    AssignedTo = fields.Char('Assigned To')
    StartDate = fields.Date('Start Date', required=False)
    EndDate = fields.Date('End Date', required=False)
    DateLine = fields.Date('Date Line', required=False)
    States = fields.Selection([
        ('todo', 'To Do'),
        ('InProgress', 'In-proress'),
        ('review', 'Review'),
        ('done', 'Done')
    ], string='todo', default='todo')
    Tags = fields.Char('Tags', required=True)
    Parent = fields.Char('Parent', required=True)