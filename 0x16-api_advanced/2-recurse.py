#!/usr/bin/python3
"""
recursive function that queries REDDIT api returning \
        a list containing the title of all hot articles given subreddit
"""

import requests

def recurse(subreddit, hot_list=[]):
    #Check valid subreddit
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = requests.get(url, headers = {'User-agent': 'Python/requests'})
    if response.status_code == 200:
        response_dict = response.json()
        hot_posts = response_dict["data"]["children"]
        for post in hot_posts:
            hot_list.append(post["data"]["title"])
        #Check for paginated results
        if response_dict["data"]["after"] is not None:
            recurse(subreddit, response_dict["data"]["after"])
        else:
            return hot_list
    else:
        return None
