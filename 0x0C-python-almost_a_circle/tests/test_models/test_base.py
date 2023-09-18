#!/usr/bin/python3

''' This module contains the class TestBase '''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    '''hold test cases for ``base.py`` '''

    def test_id(self):
        ''' tests the id '''
        b1 = Base()
        b2 = Base()
        b3 = Base(69)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 69)
