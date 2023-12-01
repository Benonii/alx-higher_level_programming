#!/usr/bin/python3

''' A module containing the function find_peak '''


def find_peak(list_of_integers):
    '''Finds the peak from a list of integers using a binary search method'''

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
        return list_of_integers[low]
