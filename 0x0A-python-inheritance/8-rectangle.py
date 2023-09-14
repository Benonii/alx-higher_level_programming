#!/usr/bin/python3

''' This module contains the class rectangle. Which inherits from BaseGeometry
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' This is a rectangle that has a width and a height
    '''

    def __init__(self, width, height):
        ''' Initialisation '''
        self.__width = width
        self.__height = height

        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
