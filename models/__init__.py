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

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()