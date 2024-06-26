#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL"""

from sys import argv
import urllib.request


if __name__ == '__main__':
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
