#!/usr/bin/python3
"""Retrieve header with requests module
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    r = requests.get(url)
    header = r.headers.get('X-Request-Id')
    print(header)
