#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from console import HBNBCommand

""" Unitest for comand interpreter """

""" These tests cover different methods in the HBNBCommand class
 and check the expected behavior of each method.

  the tests use the patch decorator from the unittest.mock module
  to simulate input and output.
   It replaces the sys.stdout with a StringIO object,
    allowing us to capture the output produced by the console commands. """


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.file_storage = FileStorage()

    def tearDown(self):
        self.console = None

    def test_do_quit(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_output.getvalue(), "")

    def test_do_EOF(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(fake_output.getvalue(), "\n")

    def test_do_create(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd("create BaseModel")
            output = fake_output.getvalue().strip()
            self.assertTrue(output)

    def test_do_show(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd("show BaseModel 12345")
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd("destroy BaseModel 12345")
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_all(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd("all")
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_do_update(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd('update BaseModel 12345 name "John Doe"')
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == "__main__":
    unittest.main()
