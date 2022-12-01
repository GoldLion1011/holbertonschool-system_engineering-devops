#!/usr/bin/python3
""" Returns information about and employee's todo list progress """
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

    with open('{}.json'.format(user_id), 'w', encoding='UTF') as f:
        todo_dict = {}
        todo_dict[sys.argv[1]] = []
        for todo in todo_list:
            task = {}
            task['task'] = todo['title']
            task['completed'] = todo['completed']
            task['username'] = u_name
            todo_dict[sys.argv[1]].append(task)

        f.write(json.dumps(todo_dict))
