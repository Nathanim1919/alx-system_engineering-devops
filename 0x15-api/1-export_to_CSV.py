#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import csv
import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = user.json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0
    csv_file_name = "{}.csv".format(userId)
    csv_header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(csv_file_name, mode='w', newline='') as csv_file:
        task_writer = csv.writer(csv_file, delimiter=',',
                                 quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todos.json():
            if task.get('userId') == int(userId):
                totalTasks += 1
                if task.get('completed'):
                    completed += 1
                task_writer.writerow([userId, name, task.get('completed'),
                                      task.get('title')])

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
