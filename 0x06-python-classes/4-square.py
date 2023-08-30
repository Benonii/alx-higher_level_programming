#!/usr/bin/python3

    '''
    A class representing a square with methods to access and set its size.

    Attributes:
        __size (int): A private field containing a positive integer that represents the length of the square.
 '''


class Square:
    '''
    A class representing a square with methods to access and set its size.

    Attributes:
        __size (int): A private field containing a positive integer that represents the length of the square.
    '''

    def __init__(self, size=0):
        '''
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's side length. Defaults to 0.

        Raises:
            ValueError: If the provided size is negative.
            TypeError: If the provided size is not an integer.
        '''
        self.__size = size

    @property
    def size(self):
        '''
        Get the size of the square.

        Returns:
            int: The size of the square's side length.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Set the size of the square.

        Args:
            value (int): The size to set for the square's side length.

        Raises:
            ValueError: If the provided size is negative.
            TypeError: If the provided size is not an integer.
        '''
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        '''
        return self.__size ** 2
