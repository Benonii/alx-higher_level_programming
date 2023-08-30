#!/usr/bin/python3

class Square:
    ''' This class takes in the length of a square and calculates the area.

    Attributes:
        size:A positive integer that represents the length of a square
        area: A method that calculates the area of the square
    '''

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
