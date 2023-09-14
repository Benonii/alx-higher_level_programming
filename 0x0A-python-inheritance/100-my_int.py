#!/usr/bin/python3

''' This module contains the class MyInt. It inhetirs from int.
    This class is a rebel for no cause. '''


class MyInt(int):
    ''' Rebel class that has everything int has. Except ``==`` is ``!=``
        and viceversa. '''

    def __eq__(self, other):
        '''returns the opposite of ``==`` '''
        return not int(self) == int(other)

    def __ne__(self, other):
        ''' returns the opposite of ``!=`` '''
        return not int(self) != int(other)
