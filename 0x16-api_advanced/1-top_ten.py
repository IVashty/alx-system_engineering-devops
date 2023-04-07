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
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Python/requests"}
    parameter = {"limit": 10}
    response = requests.get(
        url, headers=headers, parameter=parameter, allow_redirect=False
    )
    if response.status_code == 404:
        print("None")
    else:
        results = response.json().get("data")
        for child in results.get("children"):
            print(child.get("data")("title"))
