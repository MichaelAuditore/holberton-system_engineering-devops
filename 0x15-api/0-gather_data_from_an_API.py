#!/usr/bin/python3
"""Script to do a GET request to get Employee Data from an API"""
import requests
import sys

if __name__ == "__main__":
    try:
        id = int(sys.argv[1])
    except:
        exit()
    url = 'https://jsonplaceholder.typicode.com'
    try:
        name = requests.get(url + '/users/' + sys.argv[1]).json().get('name')
        todos = requests.get(url + '/todos').json()
    except ValueError:
        print("Not a valid JSON")
    ntasks = 0
    rtasks = 0
    for todo in todos:
        if todo.get('userId') == int(sys.argv[1]):
            ntasks += 1
        if (todo.get('completed') and todo.get('userId') == int(sys.argv[1])):
            rtasks += 1
    print('Employee {} is done with tasks({}/{}):'.format(name, rtasks, ntasks))
    for todo in todos:
        if (todo.get('completed') and todo.get('userId') == int(sys.argv[1])):
            print('\t{}'.format(todo.get('title')))
