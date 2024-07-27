#!/usr/bin/python3
"""The instantiates an object of class FileStorage

If equal to db:
    Import DBStorage class in this file
    Create an instance of DBStorage and store it in the variable storage
Else:
    Import FileStorage class in this file
    Create an instance of FileStorage and store it in the variable storage
"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
