#!/usr/bin/python3

''' This module contains the function inherits_from(obj, a_class)
'''


def inherits_from(obj, a_class):
    ''' Checks if obj is an instance of a subclass of a_class
    '''
    if type(obj) is a_class:
        return False

    return issubclass(type(obj), a_class)
