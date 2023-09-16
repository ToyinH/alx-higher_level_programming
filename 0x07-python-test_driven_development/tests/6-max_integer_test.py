#!/usr/bin/python3
"""unittest file for the function max_integer"""

import unittest
max_integer = __import__("6-max_integer").max_integer
class testMaxInteger(unittest.TestCase):
    """class to test max_integer"""
    def test_max_integer(self):
        """method to test for max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 3, 3]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1.0, -2, 3, 4]), 4)
