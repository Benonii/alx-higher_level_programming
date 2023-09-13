#!/usr/bin/python3

''' This module contains the function load_from_json_file
'''

import json
import os


def load_from_json_file(filename):
    ''' loads an object from a json file.
        doesn't handle exceptions. '''

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
