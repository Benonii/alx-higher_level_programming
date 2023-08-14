#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        print("{0}".format(my_list[i]))
