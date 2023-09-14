#!/usr/bin/python3

''' This module contains the function is_kind_of_class
'''


def is_kind_of_class(obj, a_class):
    ''' checks if an is an instance of a class or a super
        class '''

    return isinstance(obj, a_class)
