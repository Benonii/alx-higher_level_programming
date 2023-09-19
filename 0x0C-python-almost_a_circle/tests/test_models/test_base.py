#!/usr/bin/python3

''' This module contains the class TestBase '''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    '''hold test cases for ``base.py`` '''

    def tearDown(self):
        """
        Clean up by removing the test file if it exists.
        """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_id(self):
        ''' tests the id '''
        b1 = Base()
        b2 = Base()
        b3 = Base(69)

        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 69)

    def test_to_json_string_empty_list(self):
        ''' Checks the static method to_json string of the class Base with a an
            empty list. '''

        result = Rectangle.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_single_dict(self):
        ''' Checks the static method to_json string of the class Base with one
            dictionary. '''

        rectangle_dict = {'id': 1, 'width': 5, 'height': 4}
        result = Rectangle.to_json_string([rectangle_dict])
        expected_result = json.dumps([rectangle_dict])
        self.assertEqual(result, expected_result)

    def test_to_json_string_multiple_dicts(self):
        ''' Checks the static method to_json string of the class Base with more
            than one dictionary. '''

        rectangle_dict1 = {'id': 1, 'width': 5, 'height': 4}
        rectangle_dict2 = {'id': 2, 'width': 3, 'height': 2}
        result = Rectangle.to_json_string([rectangle_dict1, rectangle_dict2])
        expected_result = json.dumps([rectangle_dict1, rectangle_dict2])
        self.assertEqual(result, expected_result)

    def test_to_json_string_none(self):
        ''' Checks the static method to_json string of the class Base with None
        '''
        result = Rectangle.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_save_to_file(self):
        """
        Test the save_to_file method.

        - Save the list of rectangles to a file.
        - Check if the file "Rectangle.json" has been created.
        - Read the contents of the file and verify that it contains the
          expected JSON data.
        """
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)

        # Save the list of rectangles to a file
        Rectangle.save_to_file([self.r1, self.r2])

        # Check if the file "Rectangle.json" has been created
        self.assertTrue(os.path.exists("Rectangle.json"))

        # Read the contents of the file
        with open("Rectangle.json", "r") as file:
            file_contents = file.read()

        # Verify that the file contains the expected JSON data
        expected_json = (
                '[{"id": 8, "width": 10, "height": 7, "x": 2, "y": 8}, '
                '{"id": 9, "width": 2, "height": 4, "x": 0, "y": 0}]')
        self.assertEqual(file_contents, expected_json)

        def test_from_json_string_empty_string(self):
            """
            Test the from_json_string method with an empty JSON string.

            - Ensure that an empty JSON string returns an empty list.
            """
            json_string = ''
            result = Rectangle.from_json_string(json_string)
            self.assertEqual(result, [])

    def test_create(self):
        """
        Test the create method.

        - Create an instance of Rectangle using the create method.
        - Ensure that the instance has the correct attributes.
        """
        dictionary = {"id": 3, "width": 6, "height": 5, "x": 2, "y": 1}
        instance = Rectangle.create(**dictionary)
        self.assertIsInstance(instance, Rectangle)
        self.assertEqual(instance.id, 3)
        self.assertEqual(instance.width, 6)
        self.assertEqual(instance.height, 5)
        self.assertEqual(instance.x, 2)
        self.assertEqual(instance.y, 1)

    def test_load_from_file(self):
        """
        Test the load_from_file method.

        - Ensure that it returns a list of instances.
        - Verify that the returned list contains the correct number of
          instances
        - Verify that the instances in the list have the correct attributes.
        """

        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        # Save the instances to a file
        Rectangle.save_to_file([self.r1, self.r2])

        list_of_instances = Rectangle.load_from_file()
        self.assertIsInstance(list_of_instances, list)
        self.assertEqual(len(list_of_instances), 2)

        # Check the attributes of the first instance
        instance1 = list_of_instances[0]
        self.assertEqual(instance1.id, self.r1.id)
        self.assertEqual(instance1.width, self.r1.width)
        self.assertEqual(instance1.height, self.r1.height)
        self.assertEqual(instance1.x, self.r1.x)
        self.assertEqual(instance1.y, self.r1.y)

        # Check the attributes of the second instance
        instance2 = list_of_instances[1]
        self.assertEqual(instance2.id, self.r2.id)
        self.assertEqual(instance2.width, self.r2.width)
        self.assertEqual(instance2.height, self.r2.height)
        self.assertEqual(instance2.x, self.r2.x)
        self.assertEqual(instance2.y, self.r2.y)
