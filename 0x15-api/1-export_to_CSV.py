#!/usr/bin/python3
"""
 returns information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':

    # Get the spefific user with id
    User_id = int(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(User_id)).json()

    # Get the todo list of the specific userId
    payload = {'userId': User_id}
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=payload).json()
    # Data should be in the following format
    # "User_id","user_name","status","title"
    filename = f'{User_id}.csv'  # Save to a file named as user_id.csv
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([task.get('userId'), user.get('username'),
                             task.get('completed'), task.get('title')])
