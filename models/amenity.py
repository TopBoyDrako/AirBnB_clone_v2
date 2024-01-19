#!/usr/bin/python3
""" State Module for HBNB project """

from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    name: Mapped[str] = mapped_column(String(128), nullable=False)
    place_amenities: Mapped[List['Place']] = relationship(
        secondary='place_amenity', back_populates='amenities')
