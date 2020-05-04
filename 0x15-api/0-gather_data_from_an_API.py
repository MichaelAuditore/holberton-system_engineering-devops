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
    name = requests.get(url + '/users/' + sys.argv[1]).json().get('name')
    todos = requests.get(url + '/todos').json()
    ntasks = 0
    rtasks = 0
    stasks = "\n\t"
    for todo in todos:
        if todo.get('userId') == int(sys.argv[1]):
            ntasks += 1
        if (todo.get('completed') and todo.get('userId') == int(sys.argv[1])):
            rtasks += 1
            stasks += todo.get('title') + '\n\t'
    print('Employee {} is done with tasks({}/{}):{}'.format(name,
                                                            rtasks,
                                                            ntasks,
                                                            stasks[:-2]))
