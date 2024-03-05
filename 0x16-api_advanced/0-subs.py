#!/usr/bin/python3
"""
query module
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Elpastore'}
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return 0
    else:
        subredit_data = response.json().get('data')
        return subredit_data.get('subscribers')
