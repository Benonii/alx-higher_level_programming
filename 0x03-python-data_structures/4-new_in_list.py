#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list[:]
    else:
        copy_list = my_list[:]
        for i in range(len(copy_list)):
            if i == idx:
                copy_list[i] = element
        return copy_list
