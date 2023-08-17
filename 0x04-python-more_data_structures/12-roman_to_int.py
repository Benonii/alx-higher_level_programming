#!/usr/bin/python3
def roman_to_int(roman_string):
    Roman = {
            'I': 1
            'II': 2
            'III': 3
            'IV': 4
            'V': 5
            'VI': 6
            'VII': 7
            'VIII': 8
            'XI': 9
            'X': 10
            'L': 50
            'C': 100
            'D': 500
            'M': 100
            }
    number = 0
    for i in range len(roman_string):
        if roman_string[i] == 'I' and roman_string[i + 1] == 'V':
            number += Roman['IV']
        elif roman_string[i] == 'I' and roman_string[i + 1] == 'X':
            number += Roman['IX']
        else:
            number += Roman[roman_string[i]]
    return number
