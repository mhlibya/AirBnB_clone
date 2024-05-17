#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
	"""Serializes instances to a JSON file and deserializes JSON file to instances."""
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""Return the dictionary __objects."""
		return self.__objects

	def new(self, obj):
		"""Set in __objects the obj with key <obj class name>.id."""
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		__objects[key] = obj

	def save(self):
		"""Serialize __objects to the JSON file."""
		serislized_objects = {}
		for key, obj in self.__objects:
			self.__objects[key] = obj.to_dict()
		with open(self.__file_path, "w") as f:
			json.dump(serialized_objects, f)

	def reload(self):
		"""
		deserializes the JSON file to __objects, if the JSON
		file exists, otherwise nothing happens)
		"""
		try:
			with open(self.__file_path, 'r') as f:
				dict = json.loads(f.read())
			for value in dict.values():
				cls = value["__class__"]
				self.new(eval(cls)(**value))
		except Exception:
			pass
