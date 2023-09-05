#!/usr/bin/python3

'''
This module contains the function print_square.

It prints a square using ``#``
'''

def print_square(size):
    ''' 
    This fucntion prints a sqaure that has an area of size ** 2
    using  ``#``
    '''

    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif size == 0:
            print("")
        else:
            for length in range(size):
                for width in range(size):
                    print("#", end="")
                print("")
    else:
        raise TypeError("size must be an integer")
