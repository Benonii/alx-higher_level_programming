#!/usr/bin/python3

''' This module has the function lookup(obj)
'''


def lookup(obj):
    ''' This function creates a list of all the attributes of an object
    '''

    List = [attr for attr in dir(obj)]

    return List
