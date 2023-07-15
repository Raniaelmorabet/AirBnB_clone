#!/usr/bin/python3

import json


class FileStorage:
    """
    This class handles serialization and deserialization of instances to/from a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary that stores all objects by <class name>.id.

    Methods:
        all(self): Returns the dictionary of all objects.
        new(self, obj): Adds a new object to the dictionary of objects.
        save(self): Serializes the objects to the JSON file.
        reload(self): Deserializes the JSON file and updates the objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            dict: The dictionary of all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of objects.

        Args:
            obj (BaseModel): The object to add to the dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects to the JSON file.
        """
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file and updates the objects.
        If the file doesn't exist, no exception is raised.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj_dict['__class__'] = class_name
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

