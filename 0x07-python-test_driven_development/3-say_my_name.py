#!/usr/bin/python3

'''
This module has the function say_my_name that prints a formatted string
with inputted first and last names
'''

def say_my_name(first_name, last_name=""):
    '''
    prints My name is <first name> <last name>
    with <first name> being first_name
    and <last name> being last_name
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
