#!/usr/bin/python3
"""Unit tests for the `state` module.
"""

import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Tests for User class."""

    def test_is_subclass(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_str(self):
        user = User()
        string = "[{}] ({}) {}".format(type(user).__name__, user.id, user.__dict__)
        self.assertEqual(str(user), string)
        
if __name__ == "__main__":
    unittest.main()
