import odoo
import logging
import json

_logger = logging.getLogger(__name__)

class MyPetAPI(odoo.http.Controller):
    @odoo.http.route('/foo', auth='public')
    def foo_handle(self):
        return "welcome to 'foo' API!"

    @odoo.http.route('/bar', auth = 'public')
    def bar_handle(self):
        return json.dumps({
            "content": "welcome to 'bar' API!"
        })

    @odoo.http.route(['/pet/<demo>/<id>'], type = 'http', auth = "none", sitemap = False, cors = '*', csrf = False)
    def pet_handle(self, demo, id, **kw):
        model_name = "my.pet"
        try:
            registry = odoo.modules.registry.Registry(demo)
            with odoo.api.Environment.manage(), registry.cursor() as cr:
                env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
                rec = env[model_name].search([('id', '=', int(id))], limit = 1)
                response = {
                    "status": "ok",
                    "content": {
                        "name": rec.name,
                        "nickname": rec.nickname,
                        "description": rec.description,
                        "age": rec.age,
                        "weight": rec.weight,
                        "dob": rec.dob.strftime('%d%m%Y'),
                        "gender": rec.gender,
                    }
                }
        except Exception:
            response = {
                "status": "error",
                "content": "not found"
            }
        return json.dumps(response)