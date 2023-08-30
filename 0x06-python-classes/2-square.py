#!/usr/bin/python3

class Square:
    ''' This class has the attribute size.

    Attributes:
        size: a positive integer that represents the length oof the square
    '''

    try:
        def __init__(self, size=0):
            if isinstance(size, int):
                if size < 0:
                    raise ValueError("size must be >= 0")
                else:
                    self.__size = size
            else:
                raise TypeError("size must be an integer")
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
