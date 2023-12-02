#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = datetime.strptime(kwargs.get('created_at', datetime.utcnow().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = datetime.strptime(kwargs.get('updated_at', datetime.utcnow().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')

        if '__class__' in kwargs:
            del kwargs['__class__']

        if not kwargs:
            from models import storage
            storage.new(self)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {k: v for k, v in self.__dict__.items() if k != '_sa_instance_state'}
        dictionary['__class__'] = self.__class__.__name__

        # Ensure 'created_at' and 'updated_at' are datetime objects
        for date_attr in ['created_at', 'updated_at']:
            date_value = getattr(self, date_attr, None)
            if isinstance(date_value, datetime):
                dictionary[date_attr] = date_value.isoformat()
            elif isinstance(date_value, str):
                # Convert string to datetime object
                try:
                    dictionary[date_attr] = datetime.fromisoformat(date_value).isoformat()
                except ValueError:
                    # Handle invalid date string
                    dictionary[date_attr] = date_value

        return dictionary