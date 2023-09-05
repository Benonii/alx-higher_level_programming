#!/usr/bin/python3

''' unittest for max_integer([]) '''

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    ''' This class contains tests for the function max_integer '''

    def test_max(self):
        ''' tests the output of max_integer depending on different inputs '''
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-2, 0, 2]), 2)
        self.assertEqual(max_integer([-2, -3, -5]), -2)
