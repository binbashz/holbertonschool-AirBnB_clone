#!/usr/bin/python3
"""
Unit tests for Place class.
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class.
    """

    def test_inheritance(self):
        """
        Test that Place class inherits from BaseModel.
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of Place class.
        """
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


if __name__ == "__main__":
    unittest.main()
