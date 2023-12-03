#!/usr/bin/python3
''' This module fetches https://alx-intranet.hbtn.io/status '''

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as\
            response:
        html = response.read()

        print(html)

        print("Body response:")
        print(f"- type: {type(html)}")
        print(f"- content: {html}")
        print(f"- utf8 content: {html.decode('utf-8')}\n")
