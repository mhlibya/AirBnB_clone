#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
	"""A base model class representing common attributes and methods.

	Attributes:
		id (uuid.UUID): A unique identifier for the instance.
		created_at (str): The timestamp when the instance was created.
		updated_at (str): The timestamp when the instance was last updated.
	"""
	def __init__(self, *args, **kwargs):
		"""Initialize a new instance of the BaseModel class."""

		if kwargs:
			for key, value in kwargs.items():	
				if key != '__class__':
					if key in ['created_at', 'updated_at']:
						value = datetime.strptime(datetime.now().isoformat(), "%Y-%m-%dT%H:%M:%S.%f")
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now().isoformat()
			self.updated_at = self.created_at
			models.storage.new(self)

	def save(self):
		"""Update the 'updated_at' timestamp to the current time."""
		self.updated_at = datetime.now().isoformat()
		models.storage.save()

	def to_dict(self):
		"""Return a dictionary representation of the instance.

		Returns:
			dict: A dictionary containing all instance attributes.
		"""
		ob_dict = self.__dict__
		ob_dict['__class__'] = self.__class__.__name__
		return ob_dict

	def __str__(self):
		"""Return a string representation of the instance.

		Returns:
			str: A string containing the class name, id, and attributes.
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
