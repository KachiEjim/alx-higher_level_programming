#!/usr/bin/python3
"""Request id from GitHub API
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = 'https://api.github.com/user'
    user = argv[1]
    token = argv[2]
    headers = {'Authorization': f'Bearer {token}'}

    r = requests.get(url, headers=headers)
    print(r.text)
    print(r.json().get('id'))
