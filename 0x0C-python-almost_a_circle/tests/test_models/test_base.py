#!/usr/bin/python3
"""unittest for class Base"""


import unittest
from base import Base


def test_base(unittest.TestCase):
    """test case for class Base"""
    b1 = Base()
    self.assertEqual(b1, 1)
    b2 = Base()
    self.assertEqual(b2, 2)
    b3 = Base(10)
    self.assertEqual(b3, 10)
    b4 = Base()
    self.assertEqual(b4, 3)
