#!/usr/bin/python3
''' Handles error codes '''

import sys
import requests

if __name__ == '__main__':
    if requests.get(sys.argv[1]).status_code >= 400:
        print("Error code: ", requests.get(sys.argv[1]).status_code)
    else:
        print(requests.get(sys.argv[1]).text)
