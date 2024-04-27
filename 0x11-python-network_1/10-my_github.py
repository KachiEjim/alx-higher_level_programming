#!/usr/bin/python3
"""Request id from GitHub API
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = 'https://api.github.com/user'
    user = argv[1]
    token = argv[2]
    header = {f'Authorization': 'token {token}'}

    req = requests.get(url, headers=header)

    print(req.json().get('id'))
