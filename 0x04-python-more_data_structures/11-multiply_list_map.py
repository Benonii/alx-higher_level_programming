#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda x, y: x * y, my_list, number))
    return new_list
