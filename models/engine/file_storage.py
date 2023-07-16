#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os.path

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    class_name = v['__class__']
                    module_name = class_name.split('.')[0]
                    obj = eval(class_name)(**v)
                    self.__objects[k] = obj


# Update __init__.py in models directory

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


from models import storage

class BaseModel:

    def save(self):
        storage.new(self)
        storage.save()
        
    def __init__(self, *args, **kwargs):
        if kwargs:
            del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            super().__init__(*args, **kwargs)
        else:
            super().__init__()


from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
