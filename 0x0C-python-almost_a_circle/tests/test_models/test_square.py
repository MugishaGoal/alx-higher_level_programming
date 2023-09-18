#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
from models.square import Square
from io import StringIO
import sys
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_init(self):
        """Test if Square initializes correctly."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsInstance(s.id, int)
        self.assertGreater(s.id, 0)

    def test_init_with_arguments(self):
        """Test if Square initializes correctly with arguments."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 10)

    def test_size_property(self):
        """Test the size property."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        with self.assertRaises(ValueError):
            s.size = -5
        with self.assertRaises(TypeError):
            s.size = "string"

    def test_x_property(self):
        """Test the x property."""
        s = Square(5)
        s.x = 10
        self.assertEqual(s.x, 10)
        with self.assertRaises(ValueError):
            s.x = -5
        with self.assertRaises(TypeError):
            s.x = "string"

    def test_y_property(self):
        """Test the y property."""
        s = Square(5)
        s.y = 10
        self.assertEqual(s.y, 10)
        with self.assertRaises(ValueError):
            s.y = -5
        with self.assertRaises(TypeError):
            s.y = "string"

    def test_area(self):
        """Test the area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)
        s.size = 10
        self.assertEqual(s.area(), 100)

    def test_display(self):
        """Test the display method."""
        s = Square(3)
        expected_output = "###\n" \
                          "###\n" \
                          "###\n"
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test the str method."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")

    def test_update(self):
        """Test the update method."""
        s = Square(5, 2, 3, 10)
        s.update(1, 10, 20, 30, 40)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)

    def test_update_kwargs(self):
        """Test the update method with keyword arguments."""
        s = Square(5, 2, 3, 10)
        s.update(size=7, x=8, y=9, id=11)
        self.assertEqual(s.id, 11)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 9)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s = Square(5, 2, 3, 10)
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
