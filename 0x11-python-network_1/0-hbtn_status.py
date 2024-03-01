#!/usr/bin/python3
""" Fetches content from a URL using urllib and displays response details.

This script fetches content from a specified URL using the urllib package.
It then prints out details about the response,including the type of the content
the content itself, and the UTF-8 decoded content.

Usage:
    python3 -c 'print(__import__("my_module").__doc__)'

Note:
    This script requires Python 3.x and the urllib package.
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        body = response.read()
        utf8_content = body.decode("utf-8")

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(utf8_content))
