#!/usr/bin/python3
"""
 returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':

    # Get the spefific user with id
    User_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(User_id)).json()

    # Get the todo list of the specific userId
    # request with key=value ===> url+?+key=value
    # where key is userId and value id
    # todo  = requests.get(f'https://jsonplaceholder.typicode.com/todos?
    # userId={id}).json()
    payload = {'userId': User_id}
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=payload).json()

    complete_task = []
    for task in todo:
        if task.get('completed') is True:
            complete_task.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(complete_task), len(todo)))
    for complete in complete_task:
        print(f'\t {complete}')
