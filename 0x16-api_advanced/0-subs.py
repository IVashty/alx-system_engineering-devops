#!/usr/bin/python3
"""
Module contans a function that interfaces the REDDIT api & \
        requires to returns the number of subscribers from a given \
        subreddit(not active users, total subscribers)
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
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Python/requests"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
