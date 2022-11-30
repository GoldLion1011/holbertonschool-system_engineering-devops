#!/usr/bin/python3
""" Returns information about and employee's todo list progress """
import requests
import sys


def get_u_name(url, user_id):
    """ Returns user name/employee """
    response = requests.get('{}users/{}'.format(url, user_id))
    u_dict = response.json()
    return u_dict['name']


def get_todos(url, user_id):
    """ Returns user's todo list progress """
    response = requests.get('{}users/{}/todo_list'.format(url, user_id))
    return response.json()


def get_completed(todo_list):
    """ Returns user's completed items """
    done_str = ""
    done_list = []
    count = 0
    for todo in todo_list:
        if todo['completed'] is True:
            count += 1
            done_list.append('\t {}'.format(todo['title']))
    done_str = '\n'.join(done_list)
    return count, done_str


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    u_name = get_u_name(url, user_id)
    todo_list = get_todos(url, user_id)
    total = len(todo_list)
    count, done_str = get_completed(todo_list)

    print(
        'Employee {} is done with tasks:({}/{}):'.format(u_name, count, total))
    if count > 0:
        print(done_str)
