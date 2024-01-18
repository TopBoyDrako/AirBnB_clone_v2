#!/usr/bin/python3
""" Place module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False)
                      )

class Place(BaseModel, Base):
    """ Place class to store place information """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
    elif getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def reviews(self):
            """ Getter attribute for reviews in FileStorage """
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
