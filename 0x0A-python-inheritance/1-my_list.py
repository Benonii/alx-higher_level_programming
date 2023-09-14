#!/usr/bin/python3

''' This module has the class my_list that inherits from list
'''


class MyList(list):
    ''' This class contains a list of integers and it has a
        method to print a sorted copy of the list '''

    def __str__(self):
        ''' makes print() work '''

        return "{}".format(list(self))

    def print_sorted(self):
        print(sorted(self))
