#!/usr/bin/python3
"""Unit tests for the `city` module.
"""
# tests/test_models/test_place.py

import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """Tests for Place class."""

    def test_is_subclass(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_str(self):
        place = Place()
        string = "[{}] ({}) {}".format(type(place).__name__, place.id, place.__dict__)
        self.assertEqual(str(place), string)

if __name__ == "__main__":
    unittest.main()

