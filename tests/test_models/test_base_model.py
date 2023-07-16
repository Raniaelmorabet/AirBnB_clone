#!/usr/bin/python3
"""Unit testting for BaseModel"""

import unittest
import models
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""

    def test_docstring(self):
        """This is a test to check if functions, classes and modules all have docstring"""
        message = "Docstring is not present in function"
        self.assertIsNotNone(models.base_model.__doc__, message)
        message = "Docstring is not present in class"
        self.assertIsNotNone(BaseModel.__doc__, message)
    
    def test_exec_file(self):
        """Test to check if all files are executable"""
        #Check if read access
        read_true = os.access("models/base_model.py", os.R_OK)
        self.assertTrue(read_true)

        #Check if write access
        write_true = os.access("models/base_model.py", os.W_OK)
        self.assertTrue(write_true)

        #Check for executable
        exec_true = os.access("models/base_model.py", os.X_OK)
        self.assertTrue(exec_true)
    
    def test_init_BaseModel(self):
        """Test to check if object is BaseModel"""
        check_BaseModel = BaseModel()
        self.assertIsInstance(check_BaseModel, BaseModel)
    
    def test_id(self):
        """Check if the ids are unique, that is not the same"""
        first_id = BaseModel()
        second_id = BaseModel()
        self.assertNotEqual(first_id, second_id)
    
    def test_str(self):
        """Check if the output is a string"""
        str_obj = BaseModel()
        dictionary = str_obj.__dict__
        first_str = "[BaseModel] ({}) {}".format(str_obj.id, dictionary)
        second_str = str(str_obj)
        self.assertEqual(first_str, second_str)
    
    def test_save(self):
        """Check if date update is save"""
        updated = BaseModel()
        first_update = updated.updated_at
        updated.save()
        second_update = updated.updated_at
        self.assertNotEqual(first_update, second_update)
    
    def test_to_dict(self):
        """Check if to_dict added a dictionary"""
        original_model = BaseModel()
        dict_model = original_model.to_dict()
        self.assertIsInstance(dict_model, dict)
        for key, value in dict_model.items():
            check = 0
            if dict_model['__class__'] == 'BaseModel':
                check+=1
            self.assertTrue(check == 1)
        for key, value in dict_model.items():
            if key == "created_at":
                self.assertIsInstance(value, str)
            if key == "updated_at":
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
