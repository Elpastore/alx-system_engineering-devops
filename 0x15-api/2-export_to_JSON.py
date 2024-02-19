#!/usr/bin/python3
"""
 returns information about his/her TODO list progress.
 and export data in the JSON format.
"""
import csv
import json
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

            obj = []
            for task in todo_request:
                obj.append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user_request.get('username')
                })
            json_represention = {User_id: obj}
            filename = f'{User_id}.json'
            with open(filename, 'w') as file:
                json.dump(json_represention, file)
