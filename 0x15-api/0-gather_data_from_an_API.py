#!/usr/bin/python3
"""
 returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':

    if len(argv) == 2:
        # Get the spefific user with id
        User_id = int(argv[1])
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(User_id))
        # Get the todo list of the specific userId
        payload = {'userId': User_id}
        todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params=payload)
        if user.status_code == 200 and todo.status_code == 200:
            user_request = user.json()
            todo_request = todo.json()
            complete_task = []
            for task in todo_request:
                if task.get('completed') is True:
                    complete_task.append(task.get('title'))
            print("Employee {} is done with tasks({}/{}):".
                  format(user_request.get('name'), len(complete_task),
                         len(todo_request)))
            for complete in complete_task:
                print(f'\t {complete}')
