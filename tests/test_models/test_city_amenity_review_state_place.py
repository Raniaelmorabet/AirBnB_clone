#!/usr/bin/python3
"""Defines unittests for models"""

import unittest
import os
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestClasses(unittest.TestCase):
    """Test cases for the classes that inherit from BaseModel."""

    def setUp(self):
        """Set up test environment."""
        self.bm = BaseModel()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    def tearDown(self):
        """Tear down test environment."""
        del self.bm
        del self.state
        del self.city
        del self.amenity
        del self.place
        del self.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_state_inheritance(self):
        """Test State class inheritance from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_city_inheritance(self):
        """Test City class inheritance from BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_amenity_inheritance(self):
        """Test Amenity class inheritance from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_place_inheritance(self):
        """Test Place class inheritance from BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_review_inheritance(self):
        """Test Review class inheritance from BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_state_attributes(self):
        """Test State class attributes."""
        self.assertEqual(self.state.name, "")

    def test_city_attributes(self):
        """Test City class attributes."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_amenity_attributes(self):
        """Test Amenity class attributes."""
        self.assertEqual(self.amenity.name, "")

    def test_place_attributes(self):
        """Test Place class attributes."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_review_attributes(self):
        """Test Review class attributes."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
