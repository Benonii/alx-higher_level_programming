#!/usr/bin/python3
def roman_to_int(roman_string):
    Roman = {
            'I': 1,
            'II': 2,
            'III': 3,
            'IV': 4,
            'V': 5,
            'VI': 6,
            'VII': 7,
            'VIII': 8,
            'IX': 9,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 100
            }
    number = 0
    for i in range(0, len(roman_string)):
        if roman_string[i] == 'V' and roman_string[i - 1] == 'I':
            number += Roman['IV'] + 1
        elif roman_string[i] == 'X' and roman_string[i - 1] == 'I':
            number += Roman['IX'] - 1
        else:
            number += Roman[roman_string[i]]
    return number
