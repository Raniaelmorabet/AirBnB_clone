#!/usr/bin/env python3
"""
Console module for interacting with the AirBnB clone models
"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Console class for the command interpreter
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Handles empty line input
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_key = args[0] + "." + args[1]
        if instance_key in instances:
            print(instances[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_key = args[0] + "." + args[1]
        if instance_key in instances:
            del instances[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """
        if not arg:
            print([str(value) for value in storage.all().values()])
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
                return

            print([str(value) for key, value in storage.all().items()
                   if args[0] in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_key = args[0] + "." + args[1]
        if instance_key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance = instances[instance_key]
        setattr(instance, args[2], type(getattr(instance, args[2]))(args[3]))
        instance.save()

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Handles the end of file (EOF) signal to exit the program
        """
        print()
        return True

    def postloop(self):
        """
        Prints a new line after executing a command
        """
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
