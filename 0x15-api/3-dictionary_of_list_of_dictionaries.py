#!/usr/bin/python3
"""Script to do a GET request to get Employee
Data from an API and converts to JSON"""
import requests
import sys
import json


url = 'https://jsonplaceholder.typicode.com'
usernames = requests.get(url + '/users/').json()
todos = requests.get(url + '/todos').json()
dictionary = {}
with open('todo_all_employees.json', "w") as f:
    for username in usernames:
        userid = username.get('id')
        new_list = []
        for todo in todos:
            new_dict = {}
            if (todo.get('userId') == userid):
                new_dict['task'] = todo.get('title')
                new_dict['completed'] = todo.get('completed')
                new_dict['username'] = username.get('username')
                new_list.append(new_dict)
                dictionary[userid] = new_list
    json.dump(dictionary, f)
f.closed
