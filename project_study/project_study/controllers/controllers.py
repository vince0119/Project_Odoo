# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectStudy(http.Controller):
#     @http.route('/project_study/project_study/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_study/project_study/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_study.listing', {
#             'root': '/project_study/project_study',
#             'objects': http.request.env['project_study.project_study'].search([]),
#         })

#     @http.route('/project_study/project_study/objects/<model("project_study.project_study"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_study.object', {
#             'object': obj
#         })
