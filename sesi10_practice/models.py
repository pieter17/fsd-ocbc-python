from datetime import date
from config import db, ma
from marshmallow import fields


class Region(db.Model):
    __tablename__ = 'avoregion'
    __table_args__ = {'extend_existing': True}
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(255))
    avocados = db.relationship('Avocado', backref=db.backref('region', lazy='dynamic'),
                               cascade='all, delete, delete-orphan')


class Type(db.Model):
    __tablename__ = 'avotype'
    __table_args__ = {'extend_existing': True}
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    avocados = db.relationship('Avocado', backref=db.backref('type', lazy='dynamic'),
                               cascade='all, delete, delete-orphan', single_parent=True)


class Avocado(db.Model):
    __tablename__ = 'avocado'
    # __table_args__ = ({'extend_existing': True}, db.PrimaryKeyConstraint('type', 'regionid'))
    __table_args__ = (db.PrimaryKeyConstraint('type', 'regionid'), {'extend_existing': True})
    date = db.Column(db.Date)
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer, db.ForeignKey('avotype.typeid'))
    regionid = db.Column(db.Integer, db.ForeignKey('avoregion.regionid'))


class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__int__(**kwargs)

    class Meta:
        model = Avocado
        include_relationships = True
        load_instance = True

    type = fields.Nested("AvocadoTypeSchema", default=None)
    region = fields.Nested("AvocadoRegionSchema", default=None)


class AvocadoTypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__int__(**kwargs)

    typeid = fields.Int()
    type = fields.Str()


class AvocadoRegionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__int__(**kwargs)

    regionid = fields.Int()
    region = fields.Str()


class RegionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Region
        include_relationships = True
        load_instance = True

    avocados = fields.Nested("RegionAvocadoSchema", default=None)


class RegionAvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # class Meta:
    #     model = Region
    #     include_relationships = True
    #     load_instance = True

    date = fields.Date()
    avgprice = fields.Float()
    totalvol = fields.Int()
    avo_a = fields.Int()
    avo_b = fields.Float()
    avo_c = fields.Float()
    type = fields.Int()
    regionid = fields.Int()


class TypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Type
        include_relationships = True
        load_instance = True

    avocados = fields.Nested("TypeAvocadoSchema", default=None)


class TypeAvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # class Meta:
    #     model = Region
    #     include_relationships = True
    #     load_instance = True

    date = fields.Date()
    avgprice = fields.Float()
    totalvol = fields.Int()
    avo_a = fields.Int()
    avo_b = fields.Float()
    avo_c = fields.Float()
    type = fields.Int()
    regionid = fields.Int()
