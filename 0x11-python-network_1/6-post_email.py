#!/usr/bin/python3
"""A  Python script that takes in a URL and an email address, sends a POST
request to the passed URL"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    """Data to be sent in the POST request"""
    data = {'email': email}

    """Make the POST request to the URL"""
    response = requests.post(url, data=data)

    """Display the body of the response"""
    print("Your email is:", response.text)
