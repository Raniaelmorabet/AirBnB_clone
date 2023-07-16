#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class - entry point of the command interpreter
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
