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

    @patch('sys.stdout', new_callable=StringIO)
    def test_simple(self, mock_stdout):
        """Test simple"""
        console.HBNBCommand().onecmd("help")
        expected_output = """\
Documented commands (type help <topic>):
========================================
EOF  help  quit

"""
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        console.HBNBCommand().onecmd("help quit")
        expected_output = "Quit command to exit the program\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        console.HBNBCommand().onecmd("help EOF")
        expected_output = "Exit the program with EOF (Ctrl+D)\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        console.HBNBCommand().onecmd("help help")
        expected_output = (
            "List available commands with \"help\" or detailed help with \"help cmd\".\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        console.HBNBCommand().onecmd("")
        self.assertEqual(mock_stdout.getvalue(), "\n")

        console.HBNBCommand().onecmd(" ")
        self.assertEqual(mock_stdout.getvalue(), "\n")

        console.HBNBCommand().onecmd("quit")
        self.assertEqual(mock_stdout.getvalue(), "")

        console.HBNBCommand().onecmd("EOF")
        self.assertEqual(mock_stdout.getvalue(), "")

        console.HBNBCommand().onecmd("\n")
        self.assertEqual(mock_stdout.getvalue(), "\n")


if __name__ == '__main__':
    unittest.main()
