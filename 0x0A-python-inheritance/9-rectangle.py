#!/usr/bin/python3

''' This module contains the class rectangle that inherits the rectangle class
from ``8-rectangle.py`` '''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' This class has all the attributes of the previous Rectangle class plus
    more.
        It adds the implementation of area and the magic method str. '''

    def __init__(self, width, height):
        ''' Initialisation '''
        self.__width = width
        self.__height = height

        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        ''' Calculates the area of the rectangle '''
        return self.__width * self.__height

    def __str__(self):
        ''' Makes print work '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
