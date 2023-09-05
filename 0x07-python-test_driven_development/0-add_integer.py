#!/usr/bin/python3

''' A module that has a function that adds two integers '''

def add_integer(a, b=98):
    ''' adds a and b '''
    if a is None and b is None:
        raise TypeError("a and b must be integers")

    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            a = int(a)
            b = int(b)

            return a + b
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
