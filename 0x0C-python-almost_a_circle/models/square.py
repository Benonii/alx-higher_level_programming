#!/usr/bin/python3

''' This module contains the class Square and it inherits from class Rectanlge.
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' This class defines a square '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Instantization '''

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter '''

        return self.width

    @size.setter
    def size(self, size):
        ''' Size setter '''
        if isinstance(size, int):
            if size > 0:
                self.width = size
                self.height = size
            else:
                raise ValueError("width msut be > 0")
        else:
            raise TypeError("width must be an integer")

    def __str__(self):
        ''' makes print() work '''

        return "[Square] ({}) {}/{} - {}".\
               format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        ''' updates attributes '''

        attributes = ["id", "size", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
                else:
                    break
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' Returns the dictionary representation of a Sqaure '''

        square = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
            }
        return square
