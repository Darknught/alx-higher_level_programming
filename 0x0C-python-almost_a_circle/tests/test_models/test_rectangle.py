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

    def test_rectangle_attributes(self):
        """Tests if the attributes are set correctly"""
        r = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(r.__width, 10)
        self.assertEqual(r.__height, 20)
        self.assertEqual(r.__x, 30)
        self.assertEqual(r.__y, 40)
        self.assertEqual(r.id, 1)

if __name__ == "__main__":
    unittest.main()
