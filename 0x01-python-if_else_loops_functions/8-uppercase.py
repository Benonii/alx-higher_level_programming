#!/usr/bin/python3
def uppercase(str):
    i = 0
    upper = ""
    for char in str:
        if ord(char) > 96 or ord(char) < 123:
            char = chr(ord(char) - 32)

        upper += char
        i += 1
    print("{0}".format(upper))
    return(0)
