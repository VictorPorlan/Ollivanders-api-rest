from flask_restful import abort, fields, marshal_with
from repository.bd import BD


class Service:
    resource_fields = {
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }
    @staticmethod
    @marshal_with(resource_fields)
    def get_item(name):
        if not name:
            abort(404, "Es necesario un nombre de Item")
        items = BD.get_item(name)
        return items

    @staticmethod
    def get_objeto(name):
        if not name:
            abort(404, "Es necesario un nombre de Objeto")
        items = BD.get_objeto(name)

        if not items:
            abort(404, "No existe ningún item {}".format(name))
        return {"name": items.name, "sell_in": items.sell_in, "quality": items.quality}
