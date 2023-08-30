#!/usr/bin/python3

class Square:
    '''This does the same thing as 3-square.py EXCEPT

    *the size feild can be accessd through the property method
    *size was set by @size.setter

    Attributes:
        size: a private field containing a positive integer that
              represents the length of the square
        area: a method that calculates the area of the square
    '''

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
