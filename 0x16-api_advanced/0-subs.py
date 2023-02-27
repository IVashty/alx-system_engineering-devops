#!/usr/bin/python3
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
    user_agent = "My User Agent"
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
