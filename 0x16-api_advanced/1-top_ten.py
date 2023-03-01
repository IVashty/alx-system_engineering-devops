#!/usr/bin/python3
"""
function that queries the REDDIT api & prints \
        the title of the first 10 hot posts listed from a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for the given subreddit.
    Args:
        subreddit(str):subreddit to query.
    """
    user_agent = "My User Agent"
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "programming"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
