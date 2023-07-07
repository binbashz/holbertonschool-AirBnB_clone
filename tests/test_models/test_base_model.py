#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """
    def test_instance_attributes(self):
        """
        Test the instance attributes of BaseModel.
        """
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_str_method(self):
        """
        Test the __str__ method of BaseModel.
        """
        model = BaseModel()
        string = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), string)

    def test_save_method(self):
        """
        Test the save method of BaseModel.
        """
        model = BaseModel()
        prev_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(prev_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel.
        """
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertEqual(obj_dict['__class__'], "BaseModel")
        self.assertEqual(obj_dict['id'], model.id)
        self.assertEqual(obj_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], model.updated_at.isoformat())


if __name__ == "__main__":

    unittest.main()
