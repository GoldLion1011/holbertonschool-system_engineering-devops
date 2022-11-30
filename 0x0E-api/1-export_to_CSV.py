#!/usr/bin/python3
""" Returns information about and employee's TODO list progress """
import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + '/users/{}'.format(sys.argv[1])).json()
    user_id = sys.argv[1]
    user_name = user.get('username')
    todos = requests.get(url + "todos", params={'userId': user_id}).json()

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, user_name, t.get('completed'), t.get('title')]
        ) for t in todos]
