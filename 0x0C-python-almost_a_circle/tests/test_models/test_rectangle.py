#!/usr/bin/python3
"""
Unittest for class Rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test for class Rectangle"""


    def test_is_instance(self):
        """test for instance of base"""
        self.assertIsInstance(Rectangle(2, 3), Base)
        
       

    def test_error(self):
        """test for error"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(5, "6")
        with self.assertRaises(TypeError):
            Rectangle("4", 7)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, 0)
        with self.assertRaises(ValueError):
            Rectangle(-2, 5)
        with self.assertRaises(ValueError):
            Rectangle(5, -5)
        with self.assertRaises(TypeError):
            Rectangle(5, 6, "4", 5)
        with self.assertRaises(TypeError):
            Rectangle(6, 5, 7, "4")
        with self.assertRaises(ValueError):
            Rectangle(3, 2, -1, 3)
        with self.assertRaises(ValueError):
            Rectangle(2, 4, 4, -3)
        

        
