#!/usr/bin/python3
"""Return a list for all hot post in a given subreddit in REDDIT's API,
invalid subreddit should return an Empty list"""
import requests


def recurse(subreddit, hot_list=[], after=None, time=0):
    URL = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    header = {'user-agent': 'miguel/0.0.1'}
    req = requests.get(URL, headers=header, allow_redirects=False,
                       params={'after': str(after)})

    if req.status_code == 200:
        data = req.json()
        items = data['data']['children']
        if len(items) > 0:
            hot_list += items
        after = data['data']['after']
        if not after:
            return hot_list
        else:
            time += 1
            recurse(subreddit, hot_list, after, time)
    else:
        return (None)

    return hot_list
