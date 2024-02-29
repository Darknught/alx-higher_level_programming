#!/bin/bash
# A script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response. size is displayed in bytes

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL=$1

response=$(curl -s -o /dev/null -w "%{size_download} %{http_code}" $URL)
echo "$response"
