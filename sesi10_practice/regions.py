from flask import make_response, abort
from config import db
from models import Avocado, Region, RegionSchema


def read_all():
    regions = Region.query.all()
    region_schema = RegionSchema(many=True)
    data = region_schema.dump(regions)
    return data


def read_one(region_id):
    region = (Region.query.filter(Region.regionid == region_id).outerjoin(Avocado).one_or_none())

    if region is not None:
        region_schema = RegionSchema()
        data = region_schema.dump(region)
        return data


def create(region):
    region_name = region.get("region")

    existing_region = (Region.query.filter(Region.region == region_name).one_or_none())

    if existing_region is None:
        schema = RegionSchema()
        new_region = schema.load(region, session=db.session)
        db.session.add(new_region)
        db.session.commit()

        data = schema.dump(new_region)
        return data, 201


def update(regionid, region):
    update_region = Region.query.filter(Region.regionid == regionid).one_or_none()

    if update_region is not None:
        schema = RegionSchema()
        updated = schema.load(region, session=db.session)
        updated.regionid = update_region.regionid

        db.session.merge(updated)
        db.session.commit()

        data = schema.dump(update_region)
        return data, 200


def delete(regionid):
    region = Region.query.filter(Region.regionid == regionid).one_or_none()

    if region is not None:
        db.session.delete(region)
        db.session.commit()
        return make_response(f'Region {regionid} deleted', 200)
    else:
        abort(404, f'Region not foind for id: {regionid}')
