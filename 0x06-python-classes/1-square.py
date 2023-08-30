#!/usr/bin/python3

class Square:
    '''
    A class that represents a square.

    Attributes:
        __size (int): The size of the square's side length.
    '''

    def __init__(self, size=0):
        '''
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's side length. Defaults to 0.
        '''
        self.__size = size
