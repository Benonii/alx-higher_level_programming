#!/usr/bin/python3

''' This module adds arguments to a Python list,
and saves them to a file. '''

import json
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    my_list = load_from_json_file("add_item.json")
    my_list.extend(av)
    my_list = av
    save_to_json_file(my_list, "add_item.json")
