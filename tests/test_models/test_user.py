#!/usr/bin/python3
"""
Unit tests for User class.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for User class.
    """

    def test_inheritance(self):
        """
        Test that User class inherits from BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of User class.
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))


if __name__ == "__main__":
    unittest.main()
