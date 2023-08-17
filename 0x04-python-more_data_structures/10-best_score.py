#!/usr/bin/python3
def best_score(a_dictionary):
    keys = []
    for i in a_dictionary.items():
        keys.append(i)
    max = a_dict[keys[0]]
    for i, j in a_dictionary.items():
        if j > max:
            best = i
