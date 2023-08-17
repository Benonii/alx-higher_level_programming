#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    keys_to_delete = []
    for i, j in a_dictionary.items():
        if j == value:
            keys_to_delete.append(i)
    for i in keys_to_delete:
        del a_dictionary[i]
    return a_dictionary
