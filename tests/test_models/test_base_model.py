#!/usr/bin/python3

"""
Unittest for BaseModel class
"""

import unittest
import pep8
import json
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test methods"""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def tearDown(self):
        """Tear down test methods"""
        pass

    def test_pep8_base_model(self):
        """Test that checks pep8 implementation in BaseModel class"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_model_docstring(self):
        """Test docstring in BaseModel class"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_base_model_init(self):
        """Test init method in BaseModel class"""
        self.assertTrue(isinstance(self.bm1, BaseModel))
        self.assertTrue(isinstance(self.bm2, BaseModel))

    # --- Testing UUID --- #
    def test_base_model_id(self):
        """Test id attribute in BaseModel class"""
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertTrue(hasattr(self.bm2, "id"))
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_base_model_id_format(self):
        """Test id format in BaseModel class"""
        self.assertIsInstance(uuid.UUID(self.bm1.id), uuid.UUID)

    def test_base_model_id_unique(self):
        """Test id uniqueness in BaseModel class"""
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_base_model_id_type(self):
        """Test id type in BaseModel class"""
        self.assertEqual(type(self.bm1.id), str)
        self.assertEqual(type(self.bm2.id), str)

    def test_base_model_id_length(self):
        """Test id length in BaseModel class"""
        self.assertEqual(len(self.bm1.id), 36)
        self.assertEqual(len(self.bm2.id), 36)

    def test_base_model_uuid_error(self):
        """
        Tests a badly named UUID, to confirm that it is checked.
        """
        bm3 = BaseModel()
        bm3.id = 'Wrong ID'
        warn = 'badly formed hexadecimal UUID string'

        with self.assertRaises(ValueError) as msg:
            uuid.UUID(bm3.id)

        self.assertEqual(warn, str(msg.exception))

    # --- Testing datetime --- #
    def test_base_model_created_at(self):
        """Test created_at attribute in BaseModel class"""
        self.assertTrue(hasattr(self.bm1, "created_at"))
        self.assertTrue(hasattr(self.bm2, "created_at"))
        self.assertTrue(isinstance(self.bm1.created_at, datetime))
        self.assertTrue(isinstance(self.bm2.created_at, datetime))

    def test_base_model_updated_at(self):
        """Test updated_at attribute in BaseModel class"""
        self.assertTrue(hasattr(self.bm1, "updated_at"))
        self.assertTrue(hasattr(self.bm2, "updated_at"))
        self.assertTrue(isinstance(self.bm1.updated_at, datetime))
        self.assertTrue(isinstance(self.bm2.updated_at, datetime))

    # --- Testing str method --- #
    def test_base_model_str(self):
        """Test __str__ method in BaseModel class"""
        self.assertEqual(str(self.bm1), "[BaseModel] ({}) {}".
                         format(self.bm1.id, self.bm1.__dict__))
        self.assertEqual(str(self.bm2), "[BaseModel] ({}) {}".
                         format(self.bm2.id, self.bm2.__dict__))
