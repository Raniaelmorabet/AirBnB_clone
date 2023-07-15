#!/usr/bin/python3

import cmd
import models
import shlex
from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.review import Review
# from models.amenity import Amenity
# from models.place import Place


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class - entry point of the command interpreter

    Attributes:
        prompt: command prompt

    Methods:
        emptyline: do nothing when empty line is entered
        do_quit: exit the program
        do_EOF: exit the program
        do_create: create a new instance of BaseModel,
            saves it and prints the id
        do_show: prints the string representation of an
            instance based on the class name and id
        do_destroy: deletes an instance based on the class name and id
        do_all: prints all string representation of all
            instances based or not on the class name
        do_update: updates an instance based on the class name
            and id by adding or updating attribute
    """
    prompt = '(hbnb) '
    allowed_classes = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
