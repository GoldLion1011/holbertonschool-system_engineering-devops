#!/usr/bin/python3
""" Returns information about and employee's todo list progress """
import csv
import json
import requests
import sys


def get_u_name(url, user_id):
    """ Returns user name/employee """
    response = requests.get('{}users/{}'.format(url, user_id))
    u_dict = response.json()
    return u_dict['username']


def get_todos(url, user_id):
    """ Returns user's todo list progress """
    response = requests.get('{}users/{}/todos'.format(url, user_id))
    return response.json()


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    u_name = get_u_name(url, user_id)
    todo_list = get_todos(url, user_id)

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            writer.writerow(
                [user_id, u_name, todo['completed'], todo['title']])
