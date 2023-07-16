#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = self.classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Print the string representation of all instances"""
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            filtered_objs = [str(obj) for obj in objs.values() if type(obj) == self.classes[arg]]
            print(filtered_objs)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    obj = storage.all()[key]
                    setattr(obj, args[2], args[3])
                    obj.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        commands = {
            "all": self.do_all,
            "count": self.do_count
        }
        args = line.split(".")
        if len(args) > 1 and args[0] in self.classes and args[1] in commands:
            command = args[1]
            class_name = args[0]
            args = command.split("(")
            command = args[0]
            if command in commands:
                args = args[1].split(")")[0].split(", ")
                if class_name in self.classes:
                    if command == "all":
                        self.do_all(class_name)
                    elif command == "count":
                        self.do_count(class_name)
        else:
            print("*** Unknown syntax:", line)

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            count = 0
            objs = storage.all()
            for obj in objs.values():
                if type(obj) == self.classes[arg]:
                    count += 1
            print(count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
