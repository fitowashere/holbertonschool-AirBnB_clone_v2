#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
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

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        # Move this storage.new(self) to save() method
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # Remove _sa_instance_state key from dictionary if it exists.
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    # Public instance method to delete the current instance from the storage
    def delete(self):
        """Delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
    # Task 6 (End)
