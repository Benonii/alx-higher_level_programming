#!/usr/bin/python3

''' This module contains the class Student '''


class Student:
    ''' Student class. Has the following public attributes:
        first_name, last_name, age '''

    def __init__(self, first_name, last_name, age):
        ''' Instantizastion '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Turns the dict into a JSON string '''

        student_dict = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
        return student_dict
