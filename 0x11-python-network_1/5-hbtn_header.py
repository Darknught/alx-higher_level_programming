#!/usr/bin/python3
"""A script that takes ina a URL, send request to the URL and displays
the value of the variable X-Requesr-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    # Check if 'X-Request-Id' is present in the response headers
    x_req = response.headers.get('X-Request-Id')
    print(x_req)
