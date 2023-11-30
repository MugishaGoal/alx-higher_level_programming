#!/bin/bash
# A Bash script that sends a request to a URL passed as an argument
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")
echo "$status_code"
