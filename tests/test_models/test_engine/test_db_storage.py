#!/usr/bin/python3
""" Module for testing db storage"""


import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.Testcase):
    """Test cases for the DBStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.db = DBStorage()
        self.db.reload()

    def tearDown(self):
        """Remove storage file at end of tests"""
        self.db.close()

    def test_all(self):
        """Test the all method"""
        self.assertIsInstance(self.db.all(), dict)

    def test_new(self):
        """Test the new method"""
        new = BaseModel()
        new.save()
        self.assertIn(new, self.db.all().values())

    def test_save(self):
        """Test the save method"""
        new = BaseModel()
        new.save()
        self.db.save()
        self.assertIn(new, self.db.all().values())

    def test_delete(self):
        """Test the delete method"""
        new = BaseModel()
        new.save()
        self.db.delete(new)
        self.assertNotIn(new, self.db.all().values())

    def test_reload(self):
        """Test the reload method"""
        self.db.reload()
        self.assertIsInstance(self.db.all(), dict)

if __name__ == '__main__':
    unittest.main()
