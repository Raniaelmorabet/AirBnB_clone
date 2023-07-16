#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of a class, save it, and print its id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            kwargs = {}
            for arg in args[1:]:
                key, value = arg.split("=")
                kwargs[key] = value.strip("\"'")
            instance = self.classes[class_name](**kwargs)
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = class_name + "." + instance_id
            instances = storage.all()
            if key in instances:
                instance = instances[key]
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = class_name + "." + instance_id
            instances = storage.all()
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print the string representation of all instances or instances of a specific class."""
        instances = storage.all()
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
            instances = {k: v for k, v in instances.items() if isinstance(v, self.classes[arg])}
        print([str(obj) for obj in instances.values()])

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = class_name + "." + instance_id
            instances = storage.all()
            if key in instances:
                instance = instances[key]
                setattr(instance, args[2], args[3])
                instance.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
