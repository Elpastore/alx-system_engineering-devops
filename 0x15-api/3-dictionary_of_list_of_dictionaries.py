#!/usr/bin/python3
"""
Returns information about all user TODO list progress
and exports data in JSON format.
"""
import json
import requests

if __name__ == '__main__':
    user_response = requests.get('https://jsonplaceholder.typicode.com/users')

    # Raise an exception if the server response isn't successful
    if user_response.status_code == 200:
        user_data = user_response.json()
        dumped = {}

        for user in user_data:
            user_id = user['id']
            username = user['username']

            todo_response = requests.get(
                f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
            todo_data = todo_response.json()

            tasks_data = []
            for task in todo_data:
                tasks_data.append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                })

            dumped[user_id] = tasks_data

        with open('todo_all_employees.json', 'w') as f:
            json.dump(dumped, f)
