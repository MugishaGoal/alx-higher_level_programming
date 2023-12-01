#!/usr/bin/python3
"""A  Python script that takes in a URL and an email address, sends a POST
request to the passed URL"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    """Make the POST request to the URL"""
    response = requests.post(url, data=email)

    """Display the body of the response"""
    print(response.text)
