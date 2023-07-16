#!/usr/bin/python3
"""Defines the BaseModel class.

This module provides the BaseModel class, which serves as the base class for
other classes in the project. It defines common instance attributes and methods.

Attributes:
    id (str): A UUID assigned to each instance upon creation.
    created_at (datetime): The datetime when an instance is created.
    updated_at (datetime): The datetime when an instance is updated.

Methods:
    __init__(self, *args, **kwargs): Initializes a new instance of the class.
    __str__(self): Returns a string representation of the instance.
    save(self): Updates the instance's updated_at attribute and saves the changes.
    to_dict(self): Returns a dictionary representation of the instance.

"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """The BaseModel class serves as the base class for other classes.

    It defines common instance attributes and methods.

    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the class.

        Args:
            *args: Unused positional arguments.
            **kwargs: A dictionary of arguments and values for instantiation.

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # Creating a unique id
            self.created_at = datetime.now()  # Creating current time when an instance is created
            self.updated_at = datetime.now()  # Creating current time when an instance is updated
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.

        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the instance's updated_at attribute and saves the changes."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing all keys and values of the instance.

        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
