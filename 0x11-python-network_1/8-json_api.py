#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a letter
as a parameter.
Usage: ./8-json_api.py [letter]
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.RequestException as err:
        print("Request Error:", err)
    except ValueError:
        print("Not a valid JSON")
