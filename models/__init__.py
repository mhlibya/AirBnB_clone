#!/usr/bin/python3

# Initialize the storage system and reload objects from the JSON file.

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
