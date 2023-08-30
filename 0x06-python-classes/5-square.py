#!/usr/bin/python3

class Square:
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
