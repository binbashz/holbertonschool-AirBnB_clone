#!/usr/bin/python3
"""
Unit tests for State class.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for State class.
    """

    def test_inheritance(self):
        """
        Test that State class inherits from BaseModel.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of State class.
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))


if __name__ == "__main__":
    unittest.main()
