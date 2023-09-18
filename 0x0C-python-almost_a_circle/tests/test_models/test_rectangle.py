#!/usr/bin/python3

''' This is a unittest for the class Rectangle that inherits from Base class.
'''

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    ''' A class for test cases for Rectangle '''

    def test_id(self):
        ''' tests the id '''

        r1 = Rectangle(1, 1, 0, 0)
        r2 = Rectangle(2, 2, 0, 0)
        r3 = Rectangle(3, 3, 0, 0, 69)

        self.assertEqual(r1.id, 10)
        self.assertEqual(r2.id, 11)
        self.assertEqual(r3.id, 69)

    def test_width_height(self):
        ''' Tests the width and height attribute of Rectangle. '''

        r1 = Rectangle(5, 1)
        r2 = Rectangle(6, 2)

        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r2.width, 6)
        self.assertEqual(r2.height, 2)

    def test_x_y(self):
        ''' Tests x and y attributes of Rectangle '''

        r1 = Rectangle(1, 1, 0, 0)
        r2 = Rectangle(2, 2, 1, 1)
        r3 = Rectangle(3, 3, 17, 34)

        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r3.x, 17)
        self.assertEqual(r3.y, 34)

    def test_width_type(self):
        '''Tests exceptions related to the wrong type given to the width
           attribute of Rectangle. '''

        with self.assertRaisesRegex(TypeError,\
                                    "width must be an integer") as e:
            r1 = Rectangle("5", 1)
        with self.assertRaisesRegex(TypeError,\
                                    "width must be an integer") as e:
            r2 = Rectangle(None, 2)
        with self.assertRaisesRegex(TypeError,\
                                    "width must be an integer") as e:
            r3 = Rectangle(True, 3)

    def test_width_value(self):
        ''' Tests exceptions related to values less than or equal to zero being
            being assigned to the width attribute of Rectangle '''

        with self.assertRaisesRegex(ValueError, "width must be > 0") as e:
            r1 = Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0") as e:
            r2 = Rectangle(-4, 2)

    def test_height_type(self):
        ''' Tests exceptions related to the wrong type given to the height
           attribute of Rectangle. '''

        with self.assertRaisesRegex(TypeError,\
                                    "height must be an integer") as e:
            r1 = Rectangle(1, "5")
        with self.assertRaisesRegex(TypeError,\
                                    "height must be an integer") as e:
            r2 = Rectangle(2, None)
        with self.assertRaisesRegex(TypeError,\
                                    "height must be an integer") as e:
            r3 = Rectangle(3, True)

    def test_height_value(self):
        ''' Tests exceptions related to values less than or equal to zero being
            being assigned to the height attribute of Rectangle '''

        with self.assertRaisesRegex(ValueError, "height must be > 0") as e:
            r1 = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0") as e:
            r2 = Rectangle(2, -4)

    def test_x_type(self):
        ''' Tests exceptions related to the wrong type given to the x
           attribute of Rectangle. '''

        with self.assertRaisesRegex(TypeError, "x must be an integer") as e:
            r1 = Rectangle(1, 1, "5", 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer") as e:
            r2 = Rectangle(2, 2, None, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer") as e:
            r3 = Rectangle(3, 3, True, 0)

    def test_x_value(self):
        ''' Tests exceptions related to values less than zero being assigned to
            the x attribute of Rectangle '''
        
        with self.assertRaisesRegex(ValueError, "x must be >= 0") as e:
            r1 = Rectangle(1, 1, -4, 0)

    def test_y_type(self):
        ''' Tests exceptions related to the wrong type given to the y
           attribute of Rectangle. '''

        with self.assertRaisesRegex(TypeError, "y must be an integer") as e:
            r1 = Rectangle(1, 1, 0, "5")
        with self.assertRaisesRegex(TypeError, "y must be an integer") as e:
            r2 = Rectangle(2, 2, 0, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer") as e:
            r3 = Rectangle(3, 3, 0, True)

    def test_y_value(self):
        ''' Tests exceptions related to values less than zero being assigned to
            the y attribute of Rectangle '''

        with self.assertRaisesRegex(ValueError, "y must be >= 0") as e:
            r1 = Rectangle(1, 1, 0, -4)
    
    def test_area(self):
        ''' tests if the area instance method of Rectangle returns the correct
            output. '''

        r1 = Rectangle(2, 3, 1, 1)
        r2 = Rectangle(5, 6, 2, 2)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 30)

    def test_display(self):
        ''' Test if the display instance method of Rectangle returns the correct
            output. '''

        r1 = Rectangle(2, 2)
        r2 = Rectangle(5, 5)
        r3 = Rectangle(2, 2, 1)
        r4 = Rectangle(2, 2, 0, 1)
        r5 = Rectangle(2, 2, 2, 2)

        self.assertEqual(r1.display(), "##\n##\n")
        self.assertEqual(r2.display(), "#####\n#####\n")
        self.assertEqual(r3.display(), " ##\n ##\n")
        self.assertEqual(r4.display(), "\n##\n##\n")
        self.assertEqual(r5.display(), "\n\n  ##\n  ##\n")

    def test_str(self):
        ''' Test if the str instance method of Rectangle returns the correct
            output. '''

        r1 = Rectangle(4, 5, 2, 3, 1)

        self.assertEqual(print(r1),\
                         "[Rectangle] (1) 2/3 - 4/5")

    def test_update_0(self):
        r1 = Rectangle(10, 10)

        r1.update(69, 4, 5, 1, 1)

        self.assertEqual(print(r1),\
                         "[Rectangle] (69) 1/1 - 4/5")

    def test_update_1(self):
        r1 = Rectangle(10, 10)
        kwargs = {
                "width": 3,
                "height": 4,
                "id": 68,
                "x": 2,
                "y": 2
                }
        r1.update(**kwargs)
        self.assertEqual(print(r1),\
                         "[Rectangle], (68) 2/2 = 3/4")
        r1.update(69, 4, 5, 1, 1, **kwargs)
        self.assertEqual(print(r1),\
                         "[Rectangle] (69) 1/1 - 4/5")
