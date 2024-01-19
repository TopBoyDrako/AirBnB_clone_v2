#!/usr/bin/python3
""" Review module for the HBNB project """

from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = 'reviews'
    text: Mapped[str] = mapped_column(String(1024), nullable=False)
    place_id: Mapped[str] = mapped_column(
        String(60), ForeignKey('places.id'), nullable=False)
    user_id: Mapped[str] = mapped_column(
        String(60), ForeignKey("users.id"), nullable=False)

    user: Mapped['User'] = relationship(back_populates='reviews')
    place: Mapped['Place'] = relationship(back_populates='reviews')
