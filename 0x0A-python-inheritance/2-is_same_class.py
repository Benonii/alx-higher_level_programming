#!/usr/bin/python3

''' This module contains the function is_same_class
'''


def is_same_class(obj, a_class):
    ''' checks if the obj is an instance of a specific
        class. Not a super class or a sub class '''

    return type(obj) is a_class
