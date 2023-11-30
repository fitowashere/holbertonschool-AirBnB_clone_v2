#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

# Task 6 (Start)
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # id column for the database
    id = Column(String(60), nullable=False, primary_key=True)
    # created_at column for the database
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    # updated_at column for the database
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        If kwargs are provided, set them as attributes.
        Otherwise, set default attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                # & Ignore __class__ attribute
                if key == "__class__":
                    pass
                # & Convert string datetime to datetime object
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                # & Set other attributes
                else:
                    setattr(self, key, value)
        else:
            # & Set default attributes
            self.id = str(uuid.uuid4())  # & Create a unique UUID
            self.created_at = datetime.now()  # & Set the creation time to now
            self.updated_at = datetime.now()  # & Set the update time to now

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()
        # Move this storage.new(self) to save() method
        models.storage.new(self)
        models.storage.save()
    # Task 6 (End)

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
