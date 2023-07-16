#!/usr/bin/python3
""" Base model
    It has the following instance attributes
    - id: Assign a uuid when an instance is created
    - created_at: Assign the current datetime when an instance is created
    - updated_at: Assign the current datetime everytime and object is updated
"""
import uuid
import models
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other class"""

    def __init__(self, *args, **kwargs):
        """Class constructor"""
        if kwargs:
            """ kwargs = self.__dict__
                created_at and updated_at are stings in the dictionary
                datetime: used to convert these strings into datetime object
            """
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4()) #creating a unique id
            self.created_at = datetime.now() #creating current time when an instance is created
            self.updated_at = datetime.now() #creating current time when an instance is updated
            models.storage.new(self)
    
    def __str__(self):
        """" Print string method """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
    def save(self):
        """Makes update with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """This returns a dict with all the keys and values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
