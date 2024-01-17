#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    state_id = ""
    name:Mapped[int] = mapped_column(String(128), nullable=False)
    state_id:Mapped[int] = mapped_column(String(60), ForeignKey('states.id'), nullable=False)
    state:Mapped["State"] = relationship(back_populates='cities')
