#!/usr/bin/python3

''' This module contains the non empty class BaseGeometry
'''


class BaseGeometry:
    ''' this class contains the function area.
        Its job is to raise an exception when area is not
        Implemented. '''

    def area(self):
        ''' raises an exception '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Validates an integer. It checks:
            Weather value is an integer.
            Weather value is grater than or equal to 0
        '''

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
