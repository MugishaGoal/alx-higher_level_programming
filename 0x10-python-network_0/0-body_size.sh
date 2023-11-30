#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL
curl -s "$1" -w "%{size_download}\n" -o /dev/null
