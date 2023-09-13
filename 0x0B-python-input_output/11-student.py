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

    def to_json(self, attrs=None):
        ''' Turns the dict into a JSON string '''

        dict_student = {}
        student_dict = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
        if attrs is None:
            return student_dict

        if not isinstance(attrs, list):
            return student_dict

        for attribute in attrs:
            if not isinstance(attribute, str):
                return student_dict

            if hasattr(self, attribute):
                dict_student[attribute] = getattr(self, attribute)

        return dict_student

    def reload_from_json(self, json):
        ''' replaces all attributes of ``Student`` '''

        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
