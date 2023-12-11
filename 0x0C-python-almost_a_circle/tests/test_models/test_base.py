#!/usr/bin/python3
"""This is a unittest for class Base"""


import json
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class to define the testCases"""
    def test_base_class_instantiation(self):
        """Testing for base instantiation"""
        b = Base()
        self.assertIsInstance(b, Base)

    def test_to_json_string_empty(self):
        """Test Base to_json_string method with an empty list"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string(self):
        """Test Base to_json_string method with a list of dictionaries"""
        list_of_dicts = [{'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3},
                {'id': 2, 'width': 7, 'height': 7, 'x': 0, 'y': 0}]
        expected_json = """[{"id": 1, "width": 10, "height": 5, "x": 2, "y": 3}, {"id": 2, "width": 7, "height": 7, "x": 0, "y": 0}]"""
        json_string = Base.to_json_string(list_of_dicts)
        self.assertEqual(json_string, expected_json)

    def test_to_json_string_none(self):
        """test base to_json_string method with None as argument"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")


if __name__ == "__main__":
    unittest.main()
