#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


# Task 6 (Start)
class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    # Add a new column to the database called name.
    name = Column(String(128), nullable=False)
    # Add a relationship attribute with the 'city' class called cities.
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """
        Returns the list of City instances with state_id equals
        to the current State.id
        """
        # FileStorage engine inclusion.
        return [city for city in storage.all(City).values()
                if city.state_id == self.id]
# Task 6 (End)
