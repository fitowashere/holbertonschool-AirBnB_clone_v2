#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("place_name", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(int(), nullable=False, default=0)
    number_bathrooms = Column(int(), nullable=False, default=0)
    max_guest = Column(int(), nullable=False, default=0)
    price_by_night = Column(int(), nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenity = relationship("Amenity", secondary="place_amenity",
                               viewonly=False)
    amenity.ids = []
