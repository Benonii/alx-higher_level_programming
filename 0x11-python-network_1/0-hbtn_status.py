#!/usr/bin/python3
''' This module fetches https://alx-intranet.hbtn.io/status '''

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

    print("Body Response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- type: {html}")
    print(f"\t- utf8 content: {html.decode('utf-8')}")
