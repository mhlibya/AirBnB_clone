#!/usr/bin/python3
"""Unit tests for the `city` module.
"""
# tests/test_models/test_city.py

import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Tests for City class."""

    def test_is_subclass(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_name(self):
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_str(self):
        city = City()
        string = "[{}] ({}) {}".format(type(city).__name__, city.id, city.__dict__)
        self.assertEqual(str(city), string)
        
if __name__ == "__main__":
    unittest.main()

