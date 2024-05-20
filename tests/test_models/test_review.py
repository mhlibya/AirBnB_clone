#!/usr/bin/python3
"""Unit tests for the `review` module.
"""
# tests/test_models/test_review.py

import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """Tests for Review class."""

    def test_is_subclass(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_str(self):
        review = Review()
        string = "[{}] ({}) {}".format(type(review).__name__, review.id, review.__dict__)
        self.assertEqual(str(review), string)
        
if __name__ == "__main__":
    unittest.main()
