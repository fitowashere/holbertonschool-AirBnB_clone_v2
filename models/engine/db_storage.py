#!/usr/bin/python3
"""
Module defines a new engine for storing data in a
MySQL database using SQLAlchemy called DBStorage.
"""


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


# Task 6 (Start)
class DBStorage:
    # Initial private class attributes.
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiates a new DBStorage object.
        """
        # Get environment variables.
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')

        # Create engine, linking to MySQL database, and testing connection.
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        # Drop all tables if the environment variable is equal to test.
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    # Method queries all objects of a given class.
    def all(self, cls=None):
        """
        Queries all objects of a given class.
        """
        # Create a dictionary to store objects.
        objects = {}

        # If cls is given, query objects of that class.
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        # Else, query all objects.
        else:
            for cls in [User, State, City, Place, Amenity, Review]:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objects[key] = obj

        return objects

    # Method adds an object to the database.
    def new(self, obj):
        """Adds an object to the database."""
        self.__session.add(obj)

    # Method saves all changes to the database.
    def save(self):
        """Saves all changes to the database."""
        self.__session.commit()

    # Method deletes an object from the database.
    def delete(self, obj=None):
        """Deletes an object from the database."""
        if obj:
            self.__session.delete(obj)

    # Method reloads data from the database.
    def reload(self):
        """Reloads data from the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

# Task 6 (End)
