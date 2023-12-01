#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    """Make the request to the URL"""
    response = requests.get(url)

    """Get the value of the X-Request-Id header"""
    x_request_id = response.headers.get('X-Request-Id')

    """Display the value of X-Request-Id"""
    print(x_request_id)
