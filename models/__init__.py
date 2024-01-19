#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


storage_type = getenv('HBNB_TYPE_STORAGE')
storage = DBStorage() if storage_type == 'db' else FileStorage()

storage.reload()
