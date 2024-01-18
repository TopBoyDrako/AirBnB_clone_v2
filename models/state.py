#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    cities: Mapped[List['City']] = relationship(
        back_populates='state', cascade="all, delete")

    if getenv('HBNB_ENV') == 'file':
        @property
        def cities(self):
            """Gets a list of all related cities."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
