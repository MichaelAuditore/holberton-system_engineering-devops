#!/usr/bin/python3
"""Script to do a GET request to get Employee
Data from an API and converts to CSV"""
import csv
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    username = requests.get(url + '/users/' + sys.argv[1]).json()
    username = username.get('username')
    todos = requests.get(url + '/todos').json()
    with open(sys.argv[1] + '.csv', "w") as f:
        for todo in todos:
            rtask = str(todo.get('completed'))
            dtask = todo.get('title')
            if (todo.get('userId') == int(sys.argv[1])):
                writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow([sys.argv[1], username, rtask, dtask])
    f.closed
