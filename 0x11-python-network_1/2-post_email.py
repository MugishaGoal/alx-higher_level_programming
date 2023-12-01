#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter"""
import urllib.parse
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    """Encode the email parameter"""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    """Make a POST request to the URL"""
    with urllib.request.urlopen(url, data=data) as response:
        """Read and decode the body of the response"""
        content = response.read().decode('utf-8')
        print(content)
