#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage
and DBStorage, depending on the value of the environment.
"""


import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Task 6 (Start)

# If the environment variable HBNB_TYPE_STORAGE is equal to db,
# create an instance of DBStorage and store it in the variable storage.
if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
# Else, create an instance of FileStorage and store it in the variable storage.
else:
    storage = FileStorage()

storage.reload()

# Task 6 (End)
