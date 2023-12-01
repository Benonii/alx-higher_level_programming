#!/usr/bin/python3
''' Decodes the utf-8 and handles errors '''
import sys
from urllib import request, parse, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read().decode('utf-8')
            print(html)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
