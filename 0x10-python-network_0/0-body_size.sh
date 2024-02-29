#!/bin/bash
# A script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response. size is displayed in bytes

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL=$1

response=$(curl -s "$URL")
response_size=$(echo -n "$response" | wc -c)

echo "$response_size"
