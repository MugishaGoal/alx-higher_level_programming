#!/usr/bin/python3
"""Defines unittests for base.py."""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import json


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        """Test empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

        """Test list with dictionaries."""
        data = [{'id': 1, 'width': 10, 'height': 4}, {'id': 2, 'width': 5, 'height': 7}]
        json_data = Base.to_json_string(data)
        self.assertEqual(json_data, json.dumps(data))

    def test_save_to_file(self):
        """Test saving an empty list to a file."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

        """Test saving a list of Rectangle instances to a file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = json.loads(file.read())
            self.assertEqual(data[0]['id'], r1.id)
            self.assertEqual(data[1]['id'], r2.id)
        os.remove("Rectangle.json")

        """Test saving a list of Square instances to a file."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            data = json.loads(file.read())
            self.assertEqual(data[0]['id'], s1.id)
            self.assertEqual(data[1]['id'], s2.id)
        os.remove("Square.json")

    def test_from_json_string(self):
        """Test empty string."""
        self.assertEqual(Base.from_json_string(""), [])

        """Test string with JSON data."""
        json_data = '[{"id": 1, "width": 10, "height": 4}, {"id": 2, "width": 5, "height": 7}]'
        data = json.loads(json_data)
        self.assertEqual(Base.from_json_string(json_data), data)

    def test_create(self):
        """Test creating a Rectangle instance from a dictionary."""
        data = {'id': 1, 'width': 10, 'height': 4}
        r = Rectangle.create(**data)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, data['id'])
        self.assertEqual(r.width, data['width'])
        self.assertEqual(r.height, data['height'])

        """Test creating a Square instance from a dictionary."""
        data = {'id': 2, 'size': 5}
        s = Square.create(**data)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, data['id'])
        self.assertEqual(s.size, data['size'])

    def test_load_from_file(self):
        """Test loading from a non-existing file."""
        self.assertEqual(Rectangle.load_from_file(), [])

        """Test loading from a file with data."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].id, r1.id)
        self.assertIsInstance(rectangles[1], Rectangle)
        self.assertEqual(rectangles[1].id, r2.id)
        os.remove("Rectangle.json")

        """Test loading from a file with Square data."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertIsInstance(squares, list)
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].id, s1.id)
        self.assertIsInstance(squares[1], Square)
        self.assertEqual(squares[1].id, s2.id)
        os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
