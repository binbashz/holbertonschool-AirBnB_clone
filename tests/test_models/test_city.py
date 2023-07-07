#!/usr/bin/python3
"""
Unit tests for City class.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for City class.
    """

    def test_inheritance(self):
        """
        Test that City class inherits from BaseModel.
        """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of City class.
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))


if __name__ == "__main__":
    unittest.main()
