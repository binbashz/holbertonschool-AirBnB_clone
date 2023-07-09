#!/usr/bin/python3
"""
test review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for Review class"""

    def test_instance_creation(self):
        """Test if an instance of Review can be created"""
        review = Review()
        self.assertIsInstance(review, Review)


if __name__ == "__main__":
    unittest.main()
