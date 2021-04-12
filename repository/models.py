from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()
class Inventario(db.Model):
    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    sell_in = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name