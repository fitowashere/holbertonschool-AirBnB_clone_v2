#!/usr/bin/python3
import unittest
from console import HBNBCommand
from models import storage
from io import StringIO
import sys


class TestHBNBCommandCreate(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.cli = HBNBCommand()
        # Redirect stdout for capturing print statements
        self.old_stdout = sys.stdout
        self.out = StringIO()
        sys.stdout = self.out

    def tearDown(self):
        """Clean up after tests"""
        # Reset stdout
        sys.stdout = self.old_stdout
        # Remove the created file (if any)
        try:
            os.remove('file.json')
        except:
            pass

    def test_create_no_class(self):
        """Test 'create' command with no class"""
        self.cli.onecmd("create")
        self.assertIn("** class name missing **", self.out.getvalue())

    def test_create_invalid_class(self):
        """Test 'create' command with invalid class"""
        self.cli.onecmd("create MyClass")
        self.assertIn("** class doesn't exist **", self.out.getvalue())

    def test_create_valid_class(self):
        """Test 'create' command with valid class"""
        self.cli.onecmd("create BaseModel")
        output = self.out.getvalue().strip()
        self.assertTrue(len(output) > 0)

    def test_create_with_string_parameter(self):
        """Test 'create' with string parameter"""
        self.cli.onecmd('create User first_name="Fito"')
        output = self.out.getvalue().strip()
        self.assertTrue(len(output) > 0)
        new_instance = storage.all()["User." + output]
        self.assertEqual(new_instance.first_name, "Fito")

    def test_create_with_integer_parameter(self):
        """Test 'create' with integer parameter"""
        self.cli.onecmd('create Place number_rooms=30')
        output = self.out.getvalue().strip()
        self.assertTrue(len(output) > 0)
        new_instance = storage.all()["Place." + output]
        self.assertEqual(new_instance.number_rooms, 30)

    def test_create_with_float_parameter(self):
        """Test 'create' with float parameter"""
        self.cli.onecmd('create Place latitude=19.99')
        output = self.out.getvalue().strip()
        self.assertTrue(len(output) > 0)
        new_instance = storage.all()["Place." + output]
        self.assertEqual(new_instance.latitude, 19.99)

    def test_create_with_multiple_parameters(self):
        """Test 'create' with multiple parameters including string, integer, and float"""
        command = 'create Place name="Fito_Was_Here" number_rooms=25 latitude=5.9'
        self.cli.onecmd(command)
        output = self.out.getvalue().strip()
        self.assertTrue(len(output) > 0)
        
        new_instance = storage.all()["Place." + output]
        
        # Verify that each attribute was correctly assigned
        self.assertEqual(new_instance.name, "Fito Was Here")
        self.assertEqual(new_instance.number_rooms, 25)
        self.assertAlmostEqual(new_instance.latitude, 5.9)  # Use assertAlmostEqual for floats

if __name__ == "__main__":
    unittest.main()
