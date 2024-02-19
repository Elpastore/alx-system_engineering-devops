#!/usr/bin/python3
"""
 returns information about his/her TODO list progress.
"""
import csv
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

            # Data should be in the following format
            # "User_id","user_name","status","title"
            filename = f'{User_id}.csv'  # Save to a file named as user_id.csv
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                for task in todo_request:
                    writer.writerow([task.get('userId'),
                                     user_request.get('username'),
                                     task.get('completed'), task.get('title')])
