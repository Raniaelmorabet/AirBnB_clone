#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import console

class ConsoleTestCase(unittest.TestCase):
    def setUp(self):
        self.console = console.HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        self.assertTrue(self.console.onecmd('quit'))
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_eof_command(self, mock_stdout):
        self.assertTrue(self.console.onecmd('EOF'))
        self.assertEqual(mock_stdout.getvalue(), '\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_line(self, mock_stdout):
        self.assertFalse(self.console.onecmd(''))
        self.assertEqual(mock_stdout.getvalue(), '')

if __name__ == '__main__':
    unittest.main()
