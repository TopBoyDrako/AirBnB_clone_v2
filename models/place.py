#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review


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

    if getenv("HBNB_ENV") == 'file':
        @property
        def reviews(self):
            """Gets list of all reviews"""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

    amenity_ids = []
