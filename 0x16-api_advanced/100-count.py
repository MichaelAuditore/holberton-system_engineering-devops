#!/usr/bin/python3
"""Return a list for all hot post in a given subreddit in REDDIT's API,
invalid subreddit should return an Empty list"""
import requests


def count_words(subreddit, word_list, after=None, dic={}, item=0):
    """Print a list of words with the respective times appears into a string"""
    if item < 1:
        dic = {i: 0 for i in word_list}

    URL = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    header = {'user-agent': 'miguel/0.0.1'}
    req = requests.get(URL, headers=header, allow_redirects=False,
                       params={'after': str(after)})

    if req.status_code == 200:
        data = req.json()
        items = data['data']['children']
        titles = list(map(lambda x: x.get('data').get('title'), items))
        after = data['data']['after']
        for title in titles:
            title = title.split(' ')
            for sb in title:
                for word in word_list:
                    if sb.lower() == word.lower():
                        dic[word] += 1
        if after:
            count_words(subreddit, word_list, after, dic, item + 1)
        else:
            dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
            for item in dic:
                if (item[1] > 0):
                    print('{}: {}'.format(item[0], item[1]))
    else:
        print('')
