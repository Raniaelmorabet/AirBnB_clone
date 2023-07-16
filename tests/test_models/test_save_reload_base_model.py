import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class in the models module.
    """

    def setUp(self):
        """
        Set up the test case by creating a new instance of FileStorage and removing any existing JSON file.
        """
        self.storage = storage
        self.file_path = self.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """
        Clean up after the test case by removing the JSON file if it exists.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """
        Test the 'all' method of FileStorage.
        """
        objs = self.storage.all()
        self.assertEqual(type(objs), dict)
        self.assertEqual(len(objs), 0)

    def test_new(self):
        """
        Test the 'new' method of FileStorage.
        """
        my_model = BaseModel()
        self.storage.new(my_model)
        objs = self.storage.all()
        self.assertEqual(len(objs), 1)
        key = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertTrue(key in objs)
        self.assertEqual(objs[key], my_model)

    def test_save_reload(self):
        """
        Test the 'save' and 'reload' methods of FileStorage.
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        objs = self.storage.all()
        self.assertEqual(len(objs), 1)
        key = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertTrue(key in objs)
        reloaded_model = objs[key]
        self.assertEqual(reloaded_model.name, my_model.name)
        self.assertEqual(reloaded_model.my_number, my_model.my_number)

    def test_reload_nonexistent_file(self):
        """
        Test the 'reload' method of FileStorage when the JSON file doesn't exist.
        """
        self.storage.reload()
        objs = self.storage.all()
        self.assertEqual(len(objs), 0)


if __name__ == '__main__':
    unittest.main()
