#!/usr/bin/python3
"""A python script that sends a post request"""

from sys import argv as a
from urllib import request as r, parse as p

if __name__ == "__main__":
    url = a[1]
    email = {'email': a[2]}
    email = p.urlencode(email)
    email = email.encode('utf-8')
    request = r(url, data=email, method='POST')
    with r.urlopen(request) as response:
        response = response.read()
        response = response.decode('utf-8')
        print(response)
