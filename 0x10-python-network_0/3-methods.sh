#!/bin/bash
# A script that takes in a URL and displays all HTTP methods the server accept
curl -sIX OPTIONS "$1"
