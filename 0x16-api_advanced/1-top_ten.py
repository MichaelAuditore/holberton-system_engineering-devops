#!/usr/bin/python3
"""Get number of subscribers for a given subreddit in REDDIT's API,
invalid subreddit should return 0"""
import requests


def top_ten(subreddit):
    URL = 'https://www.reddit.com'
    header = {'user-agent': 'miguel/0.0.1'}
    req = requests.get(URL + '/r/' + subreddit + '/hot.json', headers=header,
                       allow_redirects=False)

    if req.status_code == 200:
        data = req.json()
        i = 0
        for item in data['data']['children']:
            if i < 10:
                print(item['data']['title'])
            else:
                break
            i += 1
    else:
        print(None)
