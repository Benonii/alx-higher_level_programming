#!/usr/bin/python3

class Square:
''' This is the same as 4-square.py EXCEPT
*It has the method that prints a square using '#'

Attributes:
    size: a private field that holds a positive integer
    area: a method that calculates the area of the square
    my_print: a method that prints the square using '#'
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

    def my_print(self):
        if self.__size == 0:
            print("")
        for height in range(0, self.__size):
            for width in range(0, self.__size):
                print("#", end="")
            print("")
