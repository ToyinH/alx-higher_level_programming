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

    def test_empty_arg(self):
        """test no argu"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """test one arg"""
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_id_instances(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 6)
        self.assertEqual(r1.id, r2.id - 1)

        r1 = Rectangle(2, 3, 4)
        r2 = Rectangle(4, 6, 7)
        self.assertEqual(r1.id, r2.id - 1)

        r1 = Rectangle(2, 5, 3, 4)
        r2 = Rectangle(4, 4, 6, 7)
        self.assertEqual(r1.id, r2.id - 1)

    def test_more_than_five_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 6, 7, 3, 6, 4, 6)
    

        

        
