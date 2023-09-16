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

