#!/usr/bin/python3
"""Get number of subscribers for a given subreddit in REDDIT's API,
invalid subreddit should return 0"""
import requests


def number_of_subscribers(subreddit):
    URL = 'https://www.reddit.com'
    header = {'user-agent': 'miguel/0.0.1'}
    req = requests.get(URL + '/r/' + subreddit + '/about.json', headers=header,
                       allow_redirects=False)

    if req.status_code == 200:
        data = req.json()
        return (data['data']['subscribers'])
    else:
        return (0)
