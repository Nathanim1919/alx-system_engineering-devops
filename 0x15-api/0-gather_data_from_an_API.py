#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()

        todos_response = requests.get(todo_url)
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task["completed"]]
        total_tasks = len(todos_data)

        print(
            "Employee {} is done with tasks({}/{}):".format(
                user_data["name"], len(completed_tasks), total_tasks
            )
        )

        for task in completed_tasks:
            print("\t {}".format(task["title"]))

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
