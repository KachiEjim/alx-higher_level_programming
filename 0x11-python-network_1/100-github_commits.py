#!/usr/bin/python3
"""Request commits via GitHub API
"""

import requests
from sys import argv

if __name__ == '__main__':

    repo = argv[1]
    owner = argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/\
commits'
    data = {'per_paage': 10}

    result = requests.get(url, data=data)

    content = result.json()

    for commit in content:
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
