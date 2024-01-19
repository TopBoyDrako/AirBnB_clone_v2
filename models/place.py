#!/usr/bin/python3
""" Place module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ Place class to store place information """
