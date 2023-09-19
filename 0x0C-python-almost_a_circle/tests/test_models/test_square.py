#!/usr/bin/python3

''' This is a unittest for the class Square that inherits from Rectangle class.
'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import io


class TestSquare(unittest.TestCase):
    ''' A class for test cases fro Square '''

    def test_id(self):
        ''' Tests the id attribute '''

        s1  = Square(1)
        s2 = Square(2)
        s3 = Square(2, 0, 0, 69)

        self.assertEqual(s1.id, 33)
        self.assertEqual(s2.id, 34)
        self.assertEqual(s3.id, 69)

    def test_size(self):
        ''' Tests that the size attribute of Square. width == size &
            height == size '''

        s1 = Square(10)
        s2 = Square(20)

        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s2.width, 20)
        self.assertEqual(s2.height, 20)

    def test_str(self):
        ''' Tests if the str instance method of Square returns the correct
            output. '''

        s1 = Square(10, 1, 2, 69)

        self.assertEqual(str(s1), "[Square] (69) 1/2 - 10")

    def test_update(self):
        ''' Tests if the str instance method of Square works proplerly with
            *args and *kwargs. '''

        s1 = Square(10)
        s1.update(68, 20, 1, 2)

        self.assertEqual(str(s1), "[Square] (68) 1/2 - 20")

        kwargs = {
                "size": 30,
                "id": 69,
                "x": 3,
                "y": 4
            }
        s1.update(**kwargs)

        self.assertEqual(str(s1), "[Square] (69) 3/4 - 30")

        s1.update(70, 40, 5, 6, **kwargs)

        self.assertEqual(str(s1), "[Square] (70) 5/6 - 40")
