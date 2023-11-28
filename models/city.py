#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


# Task 6 (Start)
class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    # Add a new column to the database called name.
    name = Column(String(128), nullable=False)
    # Add a new column to the database called state_id.
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
# Task 6 (End)
