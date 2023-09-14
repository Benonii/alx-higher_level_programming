#!/usr/bin/python3

''' This module contains the function add_attribute.
'''


def add_attribute(obj, name='', value=0):
    ''' sets value to attribute if it exists '''

    if hasattr(obj, name):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
