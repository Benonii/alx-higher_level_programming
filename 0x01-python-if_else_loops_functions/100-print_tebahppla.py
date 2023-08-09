#!/usr/bin/python3
i = 0
for letter in range(122, 96, -1):
    if i % 2 != 0:
        print(chr(letter - 32), end="")
    else:
        print(chr(letter), end="")
    i += 1
