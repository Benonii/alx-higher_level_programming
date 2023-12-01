#!/usr/bin/python3
''' uses a different requests module '''
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')

print("Body response:")
print(f"    - type: {type(response)}")
print(f"    - content: {response}")
