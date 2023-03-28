#!/usr/bin/python3
"""
Function  Queries subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and Returns
    the number of subscribers for the specified subreddit.
    Arguments:
        subreddit(str):subreddit to query.
    Returns:
        number of subscribers(int) for the subreddit
        OR
        0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Python/requests"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
