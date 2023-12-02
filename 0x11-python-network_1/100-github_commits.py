#!/usr/bin/python3
"""Fetches the most recent 10 commits of a repository from a specified
user on GitHub.
Usage: ./100-github_commits.py <repository_name> <owner_name>
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()

        commits_data = response.json()

        for commit in commits_data[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.RequestException as err:
        print("Request Error:", err)
    except ValueError:
        print("Not a valid JSON")
