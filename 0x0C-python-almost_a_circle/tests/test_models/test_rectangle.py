#!/usr/bin/python3
"""
Unittest for class Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_id(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.id, 4)
        r2 = Rectangle(4, 3)
        self.assertEqual(r2.id, 5)
        r3 = Rectangle(2, 3, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(2, 3,)
        self.assertEqual(r1.id, 4)