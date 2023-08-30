#!/usr/bin/python3

class Square:
    ''' a class that initalizes an empty variable size '''

    def __init__(self, size=0):
       '''This function initializes the private field size
          and assignes it to the inputted numebr
        '''
       self.__size = size
