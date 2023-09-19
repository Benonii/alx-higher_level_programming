#!/usr/bin/python3

''' This is a base class that will be used throughout the project.
'''

import json
import os
import csv


class Base:
    ''' Base class.
        The goal of it is to manage id attribute in all future classes to avoid
        duplication. '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Instantization '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionary):
        ''' Returns a JSON string representation of ``lsit_dictionary`` '''

        if list_dictionary is None:
            return "[]"
        else:
            return json.dumps(list_dictionary)

    @classmethod
    def save_to_file(cls, list_objs):
        '''saves the JSON string representation of ``list_objs to a file.`` '''

        filename = "{}.json".format(cls.__name__)
        list_dicts = []

        with open(filename, "w", encoding="utf-8") as f:
            for obj in list_objs:
                dict_rep = cls.to_dictionary(obj)
                list_dicts.append(dict_rep)
            json_str = cls.to_json_string(list_dicts)
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the ``json_string`` '''

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all the attributes already set '''

        instance = cls(1, 1)
        cls.update(instance, **dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        ''' returns a list of instances '''

        filename = "{}.json".format(cls.__name__)
        list_of_instances = []

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                list_of_dicts = cls.from_json_string(f.read())

                for dicts in list_of_dicts:
                    instance = cls.create(**dicts)
                    list_of_instances.append(instance)

        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' serializes in CSV '''

        filename = "{}.csv".format(cls.__name__)
        data = []

        with open(filename, "w", newline="", encoding="utf-8") as f:
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]

            writer = csv.DictWriter(f, fieldnames=fields)

            writer.writeheader()

            for obj in list_objs:
                data.append(cls.to_dictionary(obj))
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        ''' deserializes in CSV '''
        filename = "{}.csv".format(cls.__name__)

        data = []

        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                data.append(row)
        return [cls.create(**items) for items in data]
