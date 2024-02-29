#!/bin/bash
# A script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response. size is displayed in bytes

curl -s "$1" | wc -c

