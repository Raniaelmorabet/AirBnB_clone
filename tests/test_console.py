#!/usr/bin/python3

"""Unittest for console.py"""

import unittest
import pep8
import os

import console
from models.base_model import BaseModel
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test for the console"""
    def test_pep8(self):
        """Test pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0)

