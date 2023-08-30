#!/usr/bin/python3

class Square:
    try:
        def __init__(self, size=0):
            if isinstance(size, int):
                if size < 0:
                    return ValueError
                else:
                    self.__size = size
            else:
                raise TypeError

        def area(self):
            return self.__size ** 2
    except TypeError:
        print("size must be an integer")
    except ValueError:
        print("size must be >= 0")
