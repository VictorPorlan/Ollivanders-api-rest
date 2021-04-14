from flask_restful import abort, fields, marshal_with
from repository.bd import BD, Inventario, db


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
    def post_item(args):
        item = Inventario(name = args['name'], sell_in = args['sell_in'], quality = args['quality'])
        db.session.add(item)
        db.session.commit()

    @staticmethod
    def delete_item(args):
        item = db.session.query(Inventario).filter_by(name = args['name'], sell_in = args['sell_in'], quality = args['quality']).first()
        db.session.delete(item)
        db.session.commit()
        
    @staticmethod
    def inventory():
        objetos = db.session.query(Inventario).all()
        result = {"inventory": []}
        for objeto in objetos:
            result["inventory"].append({"name": objeto.name, "sell_in": objeto.sell_in, "quality": objeto.quality})
        return result