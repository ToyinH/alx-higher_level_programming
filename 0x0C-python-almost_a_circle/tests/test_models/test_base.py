#!/usr/bin/python3
"""unittest for class Base"""
import unittest
import os
from models.base import Base

# Base = __import__("..models.base").Base


class TestBase(unittest.TestCase):
    def test_base(self):
        """test case for class Base"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(10)
        self.assertEqual(b3.id, 10)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

        self.assertEqual(Base(12).id, 12)

    def test_unique_id(self):
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_change(self):
        b1 = Base()
        b1.id = 13
        self.assertEqual(b1.id, 13)



    
        
