#!/usr/bin/python3

''' This module contains the fucntion class_to_json
'''


def class_to_json(obj):
    ''' returns an dictionary description of a class
    '''

    return obj.__dict__
