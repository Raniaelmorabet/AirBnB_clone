#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes a JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary of all objects.

        Args:
            cls: Optional. If provided, returns only objects of the specified class.
        """
        if cls is None:
            return self.__objects
        else:
            cls_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    cls_objects[key] = obj
            return cls_objects

    def new(self, obj):
        """
        Sets a new object in __objects with the key <obj class name>.id.

        Args:
            obj: The object to be added to __objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if it exists).
        """
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)

                classes = {
                    'BaseModel': BaseModel,
                    'User': User
                    # Add more classes here if necessary
                }

                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = classes[class_name](**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
