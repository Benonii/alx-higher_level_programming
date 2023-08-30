#!/usr/bin/python3

'''
This module defines a simple Square class.
'''


class Square:
    '''
    A class representing a square with a positive integer size attribute.

    Attributes:
        size (int): The length of the square's side.
    '''

    try:
        def __init__(self, size=0):
            '''
            Initializes a new Square instance.

            Args:
                size (int): The size of the square's side length.
                Defaults to 0.

            Raises:
                TypeError: If the provided size is not an integer.
                ValueError: If the provided size is negative.
            '''
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
