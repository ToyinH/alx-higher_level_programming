#!/usr/bin/python3
"""
Unittest for class Rectangle
"""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """test for class Square"""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)