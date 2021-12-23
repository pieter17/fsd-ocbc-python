from datetime import date
from config import db, ma
from marshmallow import fields


class Region(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(255))
    avocados = db.relationship('Avocado', backref='region', cascade='all, delete, delete-orphan', single_parent=True)


class Type(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer)
    type = db.Column(db.String(100))
    avocados = db.relationship('Avocado', backref='region', cascade='all, delete, delete-orphan', single_parent=True)


class Avocado(db.Model):
    __tablename__ = 'avocado'
    date = db.Column(db.Date)
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer, db.ForeignKey('avotype.typeid'))
    regionid = db.Column(db.Integer, db.ForeignKey('avoregion.regionid'))


class AvocadoScheme(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__int__(**kwargs)

    class Meta:
        model = Avocado
        include_relationships = True
        load_instance = True


class RegionScheme(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Region
        include_relationships = True
        load_instance = True

    avocados = fields.Nested("RegionAvocadoScheme", default=None)
