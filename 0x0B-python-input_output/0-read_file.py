#!/usr/bin/python3

''' This module contains the function read_file
'''


def read_file(filename=""):
    ''' This function reads the contents of a file and returns
    the text contained within the file '''

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
