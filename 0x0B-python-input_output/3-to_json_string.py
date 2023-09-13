#!/usr/bin/python3

''' This module contains the function to_json_string
'''


import json

def to_json_string(my_ob):
    ''' Serializes serializable objects '''

    return json.dumps(my_ob)
