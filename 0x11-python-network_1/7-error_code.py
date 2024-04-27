#!/usr/bin/python3
"""Display response body or error message
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]

    try:
        result = requests.get(url)
        result.raise_for_status()
        print(result.text)
    except Exception:
        print('Error code: {}'.format(result.status_code))
