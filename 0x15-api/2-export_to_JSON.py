#!/usr/bin/python3
"""Script to do a GET request to get Employee
Data from an API and converts to JSON"""
import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    username = requests.get(url + '/users/' + sys.argv[1]).json()
    username = username.get('username')
    todos = requests.get(url + '/todos').json()
    new_list = []
    with open(sys.argv[1] + '.json', "w") as f:
        for todo in todos:
            new_dict = {}
            if (todo.get('userId') == int(sys.argv[1])):
                new_dict['task'] = todo.get('title')
                new_dict['completed'] = todo.get('completed')
                new_dict['username'] = username
                new_list.append(new_dict)
        json.dump({sys.argv[1]: new_list}, f)
    f.closed
