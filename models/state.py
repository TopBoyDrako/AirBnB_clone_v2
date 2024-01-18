#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='all, delete')

    if getenv('HBNB_ENV') == 'file':
        @property
        def cities(self):
            """Gets a list of all related cities."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
