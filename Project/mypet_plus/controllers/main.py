import odoo
import json
import logging
from Project.mypet.controllers.main import MyPetAPI

_logger = logging.getLogger(__name__)

class MyPetAPIInherit(odoo.http.Controller.MyPetAPI):

    @odoo.http.route()
    def foo_handle(self):
        return "ABV"

    @odoo.http.route('/bar2')
    def bar_handle(self):
        return json.dumps({
            "content": "New 'bar' API!"
        })

    @odoo.http.route()
    def pet_handle(self, demo, id, **kw):
        _logger.warning("Pet handler called~")
        result = super(MyPetAPIInherit, self).pet_handle(demo, id)
        _logger.warning("Post processing~")
        return result