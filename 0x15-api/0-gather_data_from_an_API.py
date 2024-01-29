#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID, returns"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()

    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos/{}".format(user_id)

    user_response = requests.get(user_url)
    post_response = requests.get(todo_url)


    completed_tasks = [task for task in post_response if task["completed"] is True]
    total_tasks = len(post_response)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_response["name"], len(completed_tasks), total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
