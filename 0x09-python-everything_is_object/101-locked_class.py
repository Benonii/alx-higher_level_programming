#!/usr/bin/python3

''' This module contains the class LockedClass '''


class LockedClass:
    '''This class doesn't allow any atributes to be added unless
    the attribute being added is first_name
    '''

    def __setattr__(self, name, value):
        '''
        This function sets an attrinute only if the name of the
        attribute is first_name
        '''

        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError
