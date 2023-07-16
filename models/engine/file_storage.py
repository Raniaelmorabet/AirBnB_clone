#!/usr/bin/python3

"""
This module provides a file storage that serializes instances to a JSON file (JSON.dump)
It also deserializes a JSON file to instances (JSON.load)
"""

import json


class FileStorage:
    """A file storage class that handles serialization and deserialization of instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name).from_dict(obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
