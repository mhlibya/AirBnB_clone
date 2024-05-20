#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
# tests/test_models/test_engine/test_file_storage.py

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class."""

    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        base = BaseModel()
        self.storage.new(base)
        key = "{}.{}".format(base.__class__.__name__, base.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        base = BaseModel()
        self.storage.new(base)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        self.storage.reload()
        self.assertIsInstance(self.storage.all(), dict)
        
if __name__ == "__main__":
    unittest.main()

