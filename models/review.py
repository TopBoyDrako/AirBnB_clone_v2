#!/usr/bin/python3
""" Review module for the HBNB project """

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from models.base_model import Base
from models.base_model import BaseModel


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = 'reviews'
    place_id = ""
    user_id = ""
    text:Mapped[str] = mapped_column(String(1024), nullable=False)
