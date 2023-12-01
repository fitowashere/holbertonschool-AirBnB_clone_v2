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
