#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).

Requirements:
- Uses the packages urllib and sys
- Does not import packages other than urllib and sys
- Manages urllib.error.HTTPError exceptions and prints the HTTP status code
- Does not need to check arguments passed to the script (number or type)
- Uses a with statement

Usage:
    python script.py <URL>
"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Send a request to the specified URL and retrieve response
        with urllib.request.urlopen(url) as response:
            # Read and decode the body of the response inn utf-8
            body = response.read().decode('utf-8')

        # Display the body
        print(body)

    except urllib.error.HTTPError as e:
        # If an HTTPError exception is raised, print the HTTP error code
        print("Error code:", e.code)
