#!/usr/bin/python3
"""Make a request with parameters
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    res = requests.post(url, data={'q': q})

    try:
        content = res.json()

        if not content:
            print('No result')
        else:
            print('[{}] {}'.format(content['id'], content['name']))

    except ValueError:
        print('Not a valid JSON')
