#!/bin/bash
# Use curl to send a GET request to the provided URL and display the body for a 200 status code
curl -s -o response.txt -w "%{http_code}" "$1" | awk '/^200$/ {getline; print}'
