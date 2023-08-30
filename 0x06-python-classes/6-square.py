#!/usr/bin/python3

class Square:
''' This does the same thing as 5-sqaure.py EXCEPT
*it adds whitespace to the beginnign of the printed square
 based on position[0]

Attributes:
    size: A private filed that holds a positive integer
    area: A method tha calculates the area of the square
    my_print: prints a sqaure using #
    position: a private field that holda a tuple of two positive integers
'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        if isinstance(value[0], int) and isinstance(value[1], int):
            if value[0] > 0 and value[1] > 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive\
                 integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for height in range(0, self.__size):
            print(" " * self.__position[0], end="")
            for width in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
