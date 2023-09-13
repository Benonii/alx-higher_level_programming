#!/usr/bin/python3

''' This module contains the function write_file
'''


def write_file(filename="", text=""):
    ''' writes ``text`` into filename, creates it if it doesn't exist.
        overwrites if if isn't empty '''

    with open(filename, 'w', encoding='utf-8') as f:
        for char in text:
            f.write(char)
        return f.tell()
