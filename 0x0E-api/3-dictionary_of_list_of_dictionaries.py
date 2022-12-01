#!/usr/bin/python3
""" Returns information about and employee's todo list progress """
import json
import requests
import sys


def get_u_name(url, user_id):
    """ Returns user name/employee """
    response = requests.get('{}users/{}'.format(url, user_id), verify=False)
    u_dict = response.json()
    return u_dict['username']


def get_done_list(url):
    """ Returns complete todo list """
    response = requests.get('{}todos/{}'.format(url), verify=False)
    return response.json()


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    u_dict = {}
    todo_dict = {}
    todo_list = get_done_list(url)

    with open('todo_all_employees.json', 'w') as f:
        u_name = None
        for task in todo_list:
            user_id = str(task['userId'])
            if user_id in u_dict.keys():
                u_name = u_dict[user_id]
            else:
                u_name = get_u_name(url, user_id)
                u_dict[user_id] = u_name
                todo_dict[user_id] = []

            todo = {}
            todo['task'] = task['title']
            todo['completed'] = task['completed']
            todo['username'] = u_name
            todo_dict[user_id].append(todo)

        f.write(json.dumps(todo_dict))
