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

    def test_single_argument(self):
        """Test Rectangle initialization with single argument"""
        r = Rectangle(10)

if __name__ == "__main__":
    unittest.main()
