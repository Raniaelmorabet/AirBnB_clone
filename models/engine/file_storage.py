#!/usr/bin/python3
""" This is a file storage that serializes an instance to a JSON file (JSON.dump)
    It also deserializes a JSON file to an instance (JSON.load)
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User


class FileStorage:
    """This class serializes instance to a JSON file and deserializes JSON to instance"""
    __file_path = "file.json" #string - path to the JSON file (ex: file.json)
    __objects = {} #empty dict, but will store all objects by <class name>.id

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
            all it does is to get the key of the form <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {} #creates an empty dictionary

        """Next, fill dictionary with an __objects element"""
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            """ if the JSON file (__file_path) exists"""
            with open(self.__file_path, 'r', encoding="UTF8") as file:
                for key, value in json.load(file).items():
                    attr_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attr_value
        except FileNotFoundError:
            pass
