#!/usr/bin/python3
"""
1-top_ten.py module
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Abdoulaye Sadio'}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        posts = response.json().get('data')
        for post in posts.get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
