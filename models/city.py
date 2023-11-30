#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a city for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
    """
    # Task 6 (Start)
    __tablename__ = "cities"
    # Add new column to database called name.
    name = Column(String(128), nullable=False)
    # Add new column to database called state_id.
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    # Task 6 (End)
    # Add new relationship to database called places.
    places = relationship("Place", backref="cities", cascade="all, delete")
