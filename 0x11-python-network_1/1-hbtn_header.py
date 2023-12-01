#!/usr/bin/python3
''' This module displays the value of a specific header '''
import sys
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
