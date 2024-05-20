#!/usr/bin/python3
"""Testing the `base_model` module."""
# tests/test_models/test_base_model.py

import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os
import time
import uuid

class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class."""

    def test_init(self):
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_str(self):
        base = BaseModel()
        string = "[{}] ({}) {}".format(type(base).__name__, base.id, base.__dict__)
        self.assertEqual(str(base), string)

    def test_save(self):
        base = BaseModel()
        old_updated_at = base.updated_at
        time.sleep(1)
        base.save()
        self.assertNotEqual(old_updated_at, base.updated_at)

    def test_to_dict(self):
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["id"], base.id)

if __name__ == "__main__":
    unittest.main()

