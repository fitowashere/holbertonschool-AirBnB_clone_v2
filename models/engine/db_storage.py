#!/usr/bin/python3
"""
Handles the storage when the engine depends on a MySQL database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
    Database based storage system
    """
    __engine = None
    __session = None

    classes = {"User": User, "Place": Place, "State": State, "City": City,
               "Amenity": Amenity, "Review": Review}

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries all object of the same class specified,
        or all object if the class is not specified
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """
        Adds the object to the current database session
        """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """
        Commits the changes in the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes objects from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates the current database session from the engine
        """
        Base.metadata.create_all(self.__engine)
        ses_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_factory)
        self.__session = Session()

    def close(self):
        """Closes Flask connection"""
        if self.__session is not None:
            self.__session.remove()
