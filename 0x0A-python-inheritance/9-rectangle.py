#!/usr/bin/python3

''' This module contains the class rectangle that inherits the rectangle class
from ``8-rectangle.py'' '''

BaseRectangle = __import__('8-rectangle').Rectangle


class Rectangle(BaseRectangle):
    ''' This class has all the attributes of the previous Rectangle class plus
    more.
        It adds the implementation of area and the magic method str. '''

    def area(self):
        ''' Calculates the area of the rectangle '''
        return self.__width * self.__height

    def __str__(self):
        ''' Makes print work '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
