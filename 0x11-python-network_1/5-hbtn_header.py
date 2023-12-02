#!/usr/bin/python3
''' Displays a value of a specific header '''
import sys
import requests

response = requests.get(sys.argv[1])
print(response.headers.get('X-Request-Id'))
