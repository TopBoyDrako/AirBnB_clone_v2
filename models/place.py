#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from typing import List
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey(
        'places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id: Mapped[str] = mapped_column(
        String(60), ForeignKey("cities.id"), nullable=False)
    user_id: Mapped[str] = mapped_column(
        String(60), ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    number_rooms: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0)
    number_bathrooms: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0)
    max_guest: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    price_by_night: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0)
    latitude: Mapped[float] = mapped_column(Float, nullable=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=True)

    user: Mapped['User'] = relationship(back_populates='places')
    cities: Mapped['City'] = relationship(back_populates='places')
    reviews: Mapped["Review"] = relationship(
        back_populates='place', cascade='all, delete')
    amenities: Mapped[List['Amenity']] = relationship(
        secondary='place_amenity', back_populates='place_amenities', viewonly=False)
    amenity_ids = []

    if getenv("HBNB_ENV") == 'file':
        @property
        def reviews(self):
            """Gets list of all reviews"""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Returns list of amenities"""
            amenity_list = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, values):
            """Sets amenity"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
