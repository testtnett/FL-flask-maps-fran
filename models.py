import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.types import Geometry
from shapely.geometry import Point
from geoalchemy2.shape import to_shape
from geoalchemy2.elements import WKTElement
from geoalchemy2.functions import ST_DWithin
from geoalchemy2.types import Geography
from sqlalchemy.sql.expression import cast
from geoalchemy2.shape import from_shape
from datetime import datetime

db = SQLAlchemy()

'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    database_path = os.getenv('DATABASE_URL', 'DATABASE_URL_WAS_NOT_SET?!')

    app.config["SQLALCHEMY_DATABASE_URI"] = database_path

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

    # Initial sample data:
    insert_sample_locations()

def insert_sample_locations():
    loc1 = Location(
        description='Brandenburger Tor',
        geom=Location.point_representation(
            latitude=52.516247,
            longitude=13.377711
        )
    )
    loc1.insert()

    loc2 = Location(
        description='Schloss Charlottenburg',
        geom=Location.point_representation(
            latitude=52.520608,
            longitude=13.295581
        )
    )
    loc2.insert()

    loc3 = Location(
        description='Tempelhofer Feld',
        geom=Location.point_representation(
            latitude=52.473580,
            longitude=13.405252
        )
    )
    loc3.insert()
    
def countRows():
    # c = db.session.query().count() 
    query1 = db.select(db.text('count(*) AS count_1 FROM sample_locations'))
    res = db.session.execute(query1)
    c = res.scalar()
    return c

def tableExists():
    query1 = db.select(db.text(" FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'sample_locations'"))
    res = db.session.execute(query1)
    c = res.rowcount
    return c

class SpatialConstants:
    SRID = 4326
class Location(db.Model):
    __tablename__ = 'sample_locations'

    id = Column(Integer, primary_key=True)
    description = Column(String(80))
    geom = Column(Geometry(geometry_type='POINT', srid=SpatialConstants.SRID))

    @staticmethod
    def point_representation(latitude, longitude):
        point = 'POINT(%s %s)' % (longitude, latitude)
        wkb_element = WKTElement(point, srid=SpatialConstants.SRID)
        return wkb_element

    @staticmethod
    def get_items_within_radius(lat, lng, radius):
        """Return all sample locations within a given radius (in meters)"""

        #TODO: The arbitrary limit = 100 is just a quick way to make sure
        # we won't return tons of entries at once,
        # paging needs to be in place for real usecase
        results = Location.query.filter(
            ST_DWithin(
                cast(Location.geom, Geography),
                cast(from_shape(Point(lng, lat)), Geography),
                radius)
            ).limit(100).all()

        return [l.to_dict() for l in results]

    def get_location_latitude(self):
        point = to_shape(self.geom)
        return point.y

    def get_location_longitude(self):
        point = to_shape(self.geom)
        return point.x

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'location': {
                'lng': self.get_location_longitude(),
                'lat': self.get_location_latitude()
            }
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    



class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
  content = db.Column(db.Text, nullable=False)
  # content = db.Column(db.Geometry, nullable=False)
  # user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)