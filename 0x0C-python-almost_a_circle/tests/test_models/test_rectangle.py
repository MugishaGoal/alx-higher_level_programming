#!/usr/bin/python3
"""Test_rectangle.py."""


import unittest
import io
from models.rectangle import Rectangle
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    def test_init(self):
        """Test if Rectangle initializes correctly."""
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsInstance(r.id, int)
        self.assertGreater(r.id, 0)

    def test_width_getter_setter(self):
        """Test getter and setter for width."""
        r = Rectangle(5, 10)
        r.width = 15
        self.assertEqual(r.width, 15)

    """Additional tests for width setter (invalid type and value) can be added here."""

    def test_height_getter_setter(self):
        """Test getter and setter for height."""
        r = Rectangle(5, 10)
        r.height = 25
        self.assertEqual(r.height, 25)

    """Additional tests for height setter (invalid type and value) can be added here."""

    def test_x_getter_setter(self):
        """Test getter and setter for x-coordinate."""
        r = Rectangle(5, 10, 15, 20)
        r.x = 30
        self.assertEqual(r.x, 30)

    """Additional tests for x-coordinate setter (invalid type and value) can be added here."""

    def test_y_getter_setter(self):
        """Test getter and setter for y-coordinate."""
        r = Rectangle(5, 10, 15, 20)
        r.y = 25
        self.assertEqual(r.y, 25)

    """Additional tests for y-coordinate setter (invalid type and value) can be added here."""

    def test_area(self):
        """Test calculation of rectangle's area."""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """Test displaying the rectangle."""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test the string representation of the rectangle."""
        r = Rectangle(5, 10, 15, 20, 1)
        expected_output = "[Rectangle] (1) 15/20 - 5/10"
        self.assertEqual(str(r), expected_output)

    def test_update(self):
        """Test updating attributes of the rectangle."""
        r = Rectangle(5, 10, 15, 20, 1)
        r.update(2, 7, 14, 25, 30)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 14)
        self.assertEqual(r.x, 25)
        self.assertEqual(r.y, 30)
        self.assertEqual(r.id, 2)

    def test_to_dictionary(self):
        """Test generating a dictionary representation of the rectangle."""
        r = Rectangle(5, 10, 15, 20, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 15, 'y': 20}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
