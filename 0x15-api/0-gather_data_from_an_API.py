
#!/usr/bin/python3
"""Print some Employee Data getting info from an API"""
import requests
import sys

if __name__ == '__main__':
    try:
        user_id = int(sys.argv[1])
    except:
        exit()
    url = 'https://jsonplaceholder.typicode.com'
    req = requests.get(url + '/users?id=' + sys.argv[1])

    try:
        data = req.json()
        username = data[0].get('name')
    except:
        print("Not a valid JSON")

    req = requests.get(url + '/todos?userId=' + sys.argv[1])

    try:
        todos = req.json()
        ntasks = 0
        tasks = []

        for task in todos:
            if task.get('completed') is True:
                ntasks += 1
                tasks.append(task.get('title'))
    except:
        print("Not a valid JSON")

    print("Employee {} is done with tasks({}/{}):".format(username,
                                                          ntasks,
                                                          len(todos)))
    for title in tasks:
        print("\t {}".format(title))
