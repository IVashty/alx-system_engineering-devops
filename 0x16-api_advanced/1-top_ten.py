#!/usr/bin/python3
"""
the title of the first 10 hot posts listed from a given subreddit
***optimised(naming)
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
    response = requests.get(url, headers=headers, parameter=parameter)
    if response.status_code == 404:
        print("None")
    else:
        # extract json - ok!
        results = response.json()
        # extract the list of posts from the json results - ok!
        posts = results["data"]["children"]
        for result in posts:
            # printing each result now with its title
            print(result["data"]["title"])
