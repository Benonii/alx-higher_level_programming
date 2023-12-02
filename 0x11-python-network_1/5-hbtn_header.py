#!/usr/bin/python3
''' Displays a value of a specific header '''
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
