#!/usr/bin/python3

''' This module has the class Square. It inherits the previous Square class.
'''

BaseSquare = __import__('10-square').Square


class Square(BaseSquare):
    '''Defines a sqaure, same as the inherited class. Except this class has
        the definition for ``__str__``. '''

    def __str__(self):
        return "[Sqaure] {}/{}".format(self.__size, self.__size)
