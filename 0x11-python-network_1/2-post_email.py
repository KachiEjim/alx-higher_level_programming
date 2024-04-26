#!/usr/bin/python3
"""A python script that sends a post request"""

from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    email_encoded = parse.urlencode(email)
    email_encoded = email_encoded.encode('utf-8')
    request_obj = request.Request(url, data=email_encoded, method='POST')
    with request.urlopen(request_obj) as response:
        response_data = response.read()
        response_data = response_data.decode('utf-8')
        print(response_data)
