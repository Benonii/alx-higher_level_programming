#!/usr/bin/python3
i = 0
for letter in range(122, 96, -1):
    if i % 2 != 0:
        x = 32
    else:
        x = 0
    print("{0}".format(chr(letter - x)), end="")
    i += 1
