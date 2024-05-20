#!/usr/bin/python3
"""Unit tests for the `amenity` module.
"""
# tests/test_models/test_amenity.py

import unittest
from models.amenity import Amenity
import os
from models import storage
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Tests for Amenity class."""

    def test_is_subclass(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_name(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        amenity = Amenity()
        self.assertTrue("name" in amenity.to_dict())

    def test_save(self):
        amenity = Amenity()
        old_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(old_updated_at, amenity.updated_at)

    def test_str(self):
        amenity = Amenity()
        string = "[{}] ({}) {}".format(type(amenity).__name__, amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), string)
        
if __name__ == "__main__":
    unittest.main()

