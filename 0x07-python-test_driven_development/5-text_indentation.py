#!/usr/bin/python3

''' This module has the function text_indentation '''


def text_indentation(text):
    '''
    adds two blanklines aftersfter the characters:
    ``.``, ``?`` or ``:``

    '''

    if isinstance(text, str):
        for i in range(len(text)):
            prev = text[i - 1]
            if prev == "." or prev == "?" or prev == ":":
                continue
            print(text[i], end="")
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print("\n")
                i += 2
