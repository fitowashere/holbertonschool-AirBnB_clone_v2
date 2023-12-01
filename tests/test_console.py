#!/usr/bin/python3
"""Unittest for console.py"""

import unittest
import pep8
import os
import models
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """Test HBNBCommand"""

    def setUp(self):
        """Setup"""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing setup."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """HBNBCommand testing teardown."""

        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """Test docstring."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test emptyline method."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test quit method."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """Test EOF method."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.HBNB.onecmd("EOF"))

    def test_create_errors(self):
        """Test create errors."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create asdf")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Test DBStorage")
    def test_create(self):
        """Test create method."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create City")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create City")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Amenity")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Amenity")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            self.assertTrue(len(f.getvalue()) > 0)

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            self.assertTrue(len(f.getvalue()) > 0)

    @unittest.skipIf(type(models.storage) == DBStorage, "Test DBStorage")
    def test_create_kwargs(self):
        """Test create kwargs."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)
            base_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertNotIn(base_id, output)
            self.assertIn(base_id, output)
            self.assertIn("'city_id': 'San_Francisco'", output)
            self.assertIn("'number_rooms': 3", output)
            self.assertIn("'number_bathrooms': 2.5", output)
            self.assertIn("'max_guest': 5", output)
            self.assertIn("'price_by_night': 8", output)
            self.assertIn("'latitude': 37.773972", output)

    def test_show(self):
        """Test show method."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show asdf")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show BaseModel asdf")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Test destroy method."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())

            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd("destroy asdf")
                self.assertEqual(
                    "** class doesn't exist **\n", f.getvalue())

            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd("destroy BaseModel")
                self.assertEqual(
                    "** instance id missing **\n", f.getvalue())

            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd("destroy BaseModel asdf")
                self.assertEqual(
                    "** no instance found **\n", f.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Test DBStorage")
    def test_all(self):
        """Test all method."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all BaseModel")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Test DBStorage")
    def test_update(self):
        """Test update method."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update asdf")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("update BaseModel asdf")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd('create BaseModel')
                base_id = f.getvalue().strip()

            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd("update BaseModel " + base_id)
                self.assertEqual(
                    "** attribute name missing **\n", f.getvalue())

            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd("update BaseModel " + base_id + " asdf")
                self.assertEqual(
                    "** value missing **\n", f.getvalue())


    if __name__ == "__main__":
        unittest.main()
