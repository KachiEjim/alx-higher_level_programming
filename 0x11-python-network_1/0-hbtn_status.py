#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content_type = response.headers['Content-Type']
    content = response.read()
    utf8_content = content.decode('utf-8')

print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
print(f"\t- utf8 content: {utf8_content}")
