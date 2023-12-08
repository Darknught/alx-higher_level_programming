#!/usr/bin/python3
"""Module to test for Rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test class"""
    def test_rectangle_class_inheritance(self):
        """Tests for initialization of the Rectangle class
        """
        r = Rectangle(10, 20)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)

    def assertRectangleAttributes(self, r, width, height, x, y, id):
        """helper method to assert Rectangle attributes"""
        self.assertEqual(r.width, width)
        self.assertEqual(r.height, height)
        self.assertEqual(r.x, x)
        self.assertEqual(r.id, id)

    def test_single_argument(self):
        """Test Rectangle initialization with single argument"""
        r = Rectangle(10)
        self.assertRectangleAttributes(r, 10, 10, 0, 0, None)

    def test_two_arguments(self):
        """Test Rectangle with two arguments"""
        r = Rectangle(10, 20)
        self.assertRectangleAttributes(r, 10, 20, 0, 0, None)

    def test_four_arguments(self):
        """Test Rectangle with four arguments"""
        r = Rectangle(10, 20, 30, 40)
        self.assertRectangleAttributes(r, 10, 20, 30, 40, None)

    def test_all_arguments(self):
        """Test Rectangle with all arguments"""
        r = Rectangle(10, 20, 30, 40, 1)
        self.assertRectangleAttributes(r, 10, 20, 30, 40, 1)

    def test_invalid_width(self):
        """Test handling invalid width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-10)

    def test_invalid_height(self):
        """test handling invalid height"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, -20)

    def test_invalid_x(self):
        """Test handling invalid x"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -30)

    def test_invalid_y(self):
        """Test handling invalid y"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 30, -40)

    def test_invalid_type(self):
        """Test handling invalid type"""
        with self.assertRaises(TypeError):
            r = Rectangle("not_an_integer")

if __name__ == "__main__":
    unittest.main()
