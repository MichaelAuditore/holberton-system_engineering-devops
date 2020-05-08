#!/usr/bin/python3
"""Return a list for all hot post in a given subreddit in REDDIT's API,
invalid subreddit should return an Empty list"""
import requests
from collections import OrderedDict


def count_words(subreddit, word_list, after=None, dic={}, item=0):
    if item < 1:
        dic = {i: 0 for i in word_list}

    URL = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    header = {'user-agent': 'miguel/0.0.1'}
    req = requests.get(URL, headers=header, allow_redirects=False,
                       params={'after': str(after)})

    if req.status_code == 200:
        data = req.json()
        items = data['data']['children']
        titles = [item['data']['title'] for item in items]
        after = data['data']['after']

        for title in titles:
            for word in word_list:
                dic[word] += title.count(word)

        if after:
            count_words(subreddit, word_list, after, dic, item + 1)
        else:
            dic = dict(sorted(dic.items(), reverse=True))
            for key, value in dic.items():
                if value > 0:
                    print('{}: {}'.format(key, value))
    else:
        print('\n')
