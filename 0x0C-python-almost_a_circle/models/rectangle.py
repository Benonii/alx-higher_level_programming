#!/usr/bin/python3

''' This module contains the class Rectangle.
'''

import json
from models.base import Base


class Rectangle(Base):
    ''' This class defines a rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Instantization '''

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

        if not isinstance(height, int) or height <= 0:
            raise TypeError("height must be an integer")

        if not isinstance(y, int) or y < 0:
            raise ValueError("y must be a >= integer")
    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @width.setter
    def width(self, width):
        ''' width setter '''

        if isinstance(width, int):
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, height):
        ''' height setter '''
        if isinstance(height, int):
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @x.setter
    def x(self, x):
        ''' x setter '''

        if type(x) is int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, y):
        ''' y setter '''

        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        ''' Calculates the area '''
        return self.__width * self.__height

    def __str__(self):
        ''' Makes print() work '''
        return "[Rectangle] ({}) {}/{} - {}/{}".\
               format(self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        ''' displays the rectangle using ``#`` and adds whitespace with x and y
        '''

        print("\n" * self.__y, end="")
        for h in range(self.__height):
            print(" " * self.__x, end="")
            for w in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        '''updates the attributes of an onject '''
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
                else:
                    break
        if kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        ''' Returns the dictionary representation of a Rectangle '''
        rectangle = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }
        return rectangle
