#!/usr/bin/python3
"""
test_amenity module
test case  that checks if an instance of
 the "Amenity" class can be created.
 When running this script, the test case
 will be executed and the result will be displayed.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for Amenity class"""

    def test_instance_creation(self):
        """Test if an instance of Amenity can be created"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == "__main__":
    unittest.main()
