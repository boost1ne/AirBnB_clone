#!/usr/bin/pyton3
"""
This is a TestBasemodel that includes
all needed tests methodes
"""
import unittest
from models.base_model import BaseModel

class TestBasemodel(unittest.TestCase):
    """
    TestBasemodel class
    """
    def test_init(self):
        """
        Test initialization of BaseModel
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test save method
        """
        my_model = BaseModel()

        initial_update_at = my_model.updated_at

        current_updated_at = my_model.save()

        self.assertNotEqual(initial_update_at, current_updated_at)

    def test_to_dict(self):
        """
        Test to_dict method
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        """
        Test __str__ method
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == '__main__':
    unittest.main()