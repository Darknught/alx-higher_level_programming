#!/usr/bin/python3
"""This is a unittest for def max_integer([...])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerFunction(unittest.TestCase):
    """Class to define the testCases"""
    def test_module_docstring(self):
        """Tests for module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_empty_list(self):
        """Checks if the list is empty"""
        self.assertIsNone(max_integer([]), "Empty list should return None")

    def test_positive_integers(self):
        """Checks if the list is positive"""
        self.assertEqual(max_integer([1, 3, 5, 2]), 5)

    def test_negative_integers(self):
        """Checks for negative integers"""
        self.assertEqual(max_integer([-1, -3, -5, -2]), -1)

    def test_mixed_integers(self):
        """Tests for max integer in list"""
        self.assertEqual(max_integer([-1, 3, -5, 2]), 3)

    def test_single_element(self):
        """Tests for an only element in list"""
        self.assertEqual(max_integer([42]), 42)

    def test_repeated_max(self):
        """Tests for max integer repeated"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_mixed_types(self):
        """Tests for non-integer type in list"""
        with self.assertRaises(TypeError):
            max_integer(["a", 2, 3, 4])

    def test_empty_list_default_param(self):
        """Tests for empty list"""
        self.assertIsNone(max_integer())

    def test_max_at_end(self):
        """Tests for max integer at the end of list"""
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_none(self):
        """Tests for passing None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
