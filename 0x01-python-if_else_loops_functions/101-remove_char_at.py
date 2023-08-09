#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    newStr = ""
    for letter in str:
        if i == n:
            i += 1
            continue
        newStr += letter
        i += 1
    return (newStr)
