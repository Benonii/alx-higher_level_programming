#!/usr/bin/python3

''' This module contains the function append_write
'''


def append_write(filename="", text=""):
    ''' appends ``text`` to the file ``filename``
        doesn't handle any exceptions '''

    chars = 0
    with open(filename, 'a', encoding='utf-8') as f:
        for char in text:
            f.write(char)
            chars += 1
    return chars
