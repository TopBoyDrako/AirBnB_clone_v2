#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


storage_type = getenv('HBNB_TYPE_STORAGE')
storage = DBStorage() if storage_type == 'db' else FileStorage()

storage.reload()
