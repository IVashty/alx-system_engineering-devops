#!/usr/bin/python3
"""

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
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Python/requests"}
    parameter = {"limit": 10}
    response = requests.get(
        url, headers=headers, parameter=parameter, allow_redirect=False
    )
    if response.status_code == 400:
        print("None")
        return
    results = response.json().get("data")
    [print(child.get("data").get("title")) for child in results.get("children")]
