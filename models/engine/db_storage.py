#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """
        Represents the database storage
    """

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all objects depending on class"""
        instances = self.__session.query(State).all()
        instances.extend(self.__session.query(City).all())
        instances.extend(self.__session.query(Amenity).all())
        instances.extend(self.__session.query(Place).all())
        instances.extend(self.__session.query(Review).all())
        instances.extend(self.__session.query(User).all())

        return {f'{type(instance).__name__}.{instance.id}': instance for instance in instances}

    def new(self, obj):
        """Adds object to session"""
        self.__session.add(obj)

    def save(self):
        """Save changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Remove obj from database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and initialize the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close session"""
        self.__session.remove()
