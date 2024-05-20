#!/usr/bin/python3
"""Unit tests for the `state` module.
"""
# tests/test_models/test_state.py

import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Tests for State class."""

    def test_is_subclass(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_name(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_str(self):
        state = State()
        string = "[{}] ({}) {}".format(type(state).__name__, state.id, state.__dict__)
        self.assertEqual(str(state), string)
        
if __name__ == "__main__":
    unittest.main()

