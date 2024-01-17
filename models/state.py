#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from typing import List
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City

class State(BaseModel):
    """ State class """

    __tablename__ = 'states'
    name:Mapped[int] = mapped_column(String(128), nullable=False)

    if getenv('HBNB_ENV') == 'db':
        cities:Mapped[List["City"]] = relationship(back_populates="state", cascade='all, delete')
    elif getenv('HBNB_ENV') == 'file':
        @property
        def cities(self):
            """Gets a list of all related cities."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
