#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content_type = response.headers['Content-Type']
    content = response.read()
    utf8_content = content.decode('utf-8')

print("Body response:")
print(f"    - type: {type(content)}")
print(f"    - content: {content}")
print(f"    - utf8 content: {utf8_content}")
