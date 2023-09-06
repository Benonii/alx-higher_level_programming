#!/usr/bin/python3

''' A module that has a function that adds two integers.
It's name is is add_integer
'''


def add_integer(a, b=98):
    ''' adds a and b
    a and b must be non-empty ints or floats.
    a float is converted to an int before additon
    '''
    if a is None:
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
