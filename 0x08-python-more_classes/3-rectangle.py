#!/usr/bin/python3

''' This module contains the class Rectangle, and it isn't empty '''

class Rectangle:
    ''' This class defines the width and height of a rectangle '''

    def __init__(self, width=0, height=0):
        '''
        This function provides an alternate instantization with
        private attributes width and height
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @property
    def height(self):
        ''' height getter '''
        return self.__height


    @width.setter
    def width(self, value):
        ''' width setter '''
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        '''height setter '''
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        ''' calculates the area of the rectangle '''
        return self.__width * self.__height

    def perimeter(self):
        ''' calculates the perimeter of the rectangle '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self__width + self.__height)

    def __str__(self):
        ''' returns a rectangle made up of ``#`` '''
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__hegiht):
            for j in range(self.__width):
                rectangle += rectangle + "#"
            rectangle += rectangle + "\n"
        return rectangle
