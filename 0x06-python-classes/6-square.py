#!/usr/bin/python3

    '''
    A class representing a square with methods to access and set its size, position, calculate its area,
    and print it using '#'.

    Attributes:
        __size (int): A private field containing a positive integer that represents the length of the square's side.
        __position (tuple): A private field containing a tuple of 2 positive integers representing the position.
    '''

class Square:
    '''
    A class representing a square with methods to access and set its size, position, calculate its area,
    and print it using '#'.

    Attributes:
        __size (int): A private field containing a positive integer that represents the length of the square's side.
        __position (tuple): A private field containing a tuple of 2 positive integers representing the position.
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's side length. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            ValueError: If the provided size is negative.
            TypeError: If the provided size is not an integer.
            TypeError: If the provided position is not a tuple of 2 positive integers.
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''
        Get the size of the square.

        Returns:
            int: The size of the square's side length.
        '''
        return self.__size

    @property
    def position(self):
        '''
        Get the position of the square.

        Returns:
            tuple: The position of the square.
        '''
        return self.__position

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

    @position.setter
    def position(self, value):
        '''
        Set the position of the square

