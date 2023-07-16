#!/usr/bin/python3

"""Unittest for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
import pep8

import console
from models.base_model import BaseModel
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test for the console"""

    def test_pep8(self):
        """Test PEP 8 style compliance"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0)

    def test_simple(self):
        """Test simple"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue(), """
Documented commands (type help <topic>):
========================================
EOF  help  quit

""")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), "Quit command to exit "
                                           "the program\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), "EOF command to exit the program\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertEqual(f.getvalue(),
                             "List available commands with "
                             "\"help\" or detailed help with \"help cmd\".\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(" ")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
