#!/usr/bin/python3

'''
This module defines a simple Square class.
'''

class Square:
    '''
    A class that represents a square and calculates its area.

    Attributes:
        size (int): A positive integer that represents the length of a square side.
    '''

    try:
        def __init__(self, size=0):
            '''
            Initializes a new Square instance.

            Args:
                size (int): The size of the square's side length. Defaults to 0.

            Raises:
                TypeError: If the provided size is not an integer.
                ValueError: If the provided size is negative.
            '''
            if isinstance(size, int):
                if size < 0:
                    return ValueError("size must be >= 0")
                else:
                    self.__size = size
            else:
                raise TypeError("size must be an integer")

        def area(self):
            '''
            Calculate the area of the square.

            Returns:
                int: The area of the square.
            '''
            return self.__size ** 2
    except TypeError:
        print("size must be an integer")
    except ValueError:
        print("size must be >= 0")

