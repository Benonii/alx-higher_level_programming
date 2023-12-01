#!/usr/bin/python3
''' This module sends an email to the server '''
import sys
from urllib import request, parse

if __name__ == '__main__':
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    encoded_data = parse.urlencode(data).encode('utf-8')

    with request.urlopen(url, encoded_data) as response:
        html = response.read().decode('utf-8')
        print(str(html))
