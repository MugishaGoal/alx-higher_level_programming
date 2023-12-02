#!/usr/bin/python3
"""Uses GitHub API to display user id.
Usage: ./10-my_github.py <username> <personal_access_token>
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    url = "https://api.github.com/MugishaGoal"

    """Set up the authentication header"""
    auth = (username, personal_access_token)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()

        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id if user_id is not None else "None")
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.RequestException as err:
        print("Request Error:", err)
    except ValueError:
        print("Not a valid JSON")
