#!/usr/bin/python3
"""This is a unittest for class Base"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class to define the testCases"""
    def test_base_class_instantiation(self):
        """Testing for base instantiation"""
        b = Base()
        self.assertIsInstance(b, Base)

if __name__ == "__main__":
    unittest.main()
