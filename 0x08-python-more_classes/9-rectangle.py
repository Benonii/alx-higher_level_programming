#!/usr/bin/python3

''' This module contains the class Rectangle, and it isn't empty '''


class Rectangle:
    ''' This class defines the width and height of a rectangle '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''
        This function provides an alternate instantization with
        private attributes width and height
        '''

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @width.setter
    def width(self, value):
        ''' width setter '''
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        '''height getter '''
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        ''' calculates the area of the rectangle '''

        return self.__width * self.__height

    def perimeter(self):
        ''' calculates the perimeter of the rectangle '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        ''' returns a rectangle made up of ``#`` '''
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for height in range(self.__height):
            for width in range(self.__width):
                rectangle += "{}".format(Rectangle.print_symbol)
            if height != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        ''' returns a replicable string representation of a rectangle '''
        rectangle = 'Rectangle(' + str(self.__width) + ',' + \
                    str(self.__height) + ')'
        return rectangle

    def __del__(self):
        ''' is called when an instance is deleted '''
        Rectangle.number_of_instances -= 1
        print("Bye Rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' compares the areas of two rectangles and
        returms the bigger rectangle
        '''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        ''' creates a new instance of a rectangle that is a square '''
        return cls(size, size)
