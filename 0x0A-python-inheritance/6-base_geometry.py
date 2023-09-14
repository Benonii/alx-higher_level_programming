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
