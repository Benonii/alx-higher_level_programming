#!/usr/bin/python3

''' This module contains the class Square.It inherits from the class Rectangle.
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' defines a square '''

    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)

        super().integer_validator("size", size)

    def area(self):
        return self.__size ** 2
