#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None   
    keys = list(a_dictionary.keys())

    max = a_dictionary[keys[0]]
    for i, j in a_dictionary.items():
        if j > max:
            best = i
            max = j
    return best
