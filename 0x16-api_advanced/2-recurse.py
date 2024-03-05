#!/usr/bin/python3
"""
2-recurse.py module
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Elpastore"}
    params = {"limit": 100, "after": after}

    response = requests.get(url,  headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        for post in data.get("children"):
            hot_list.append(post.get("data").get("title"))
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
