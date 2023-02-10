#!/usr/bin/python3
"""
This script retrieves information about \
        the tasks of an employee from a REST API
The REST API provides information and\
        exports the data in JSON format in the format:
    { "USER_ID": [
    {"task": "TASK_TITLE","completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    ... ]
    }

file name is formatted as USER_ID.json
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    tasks = []
    content = {}
    file_name = "{}.json".format(employee_id)
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todo_list = requests.get("{}/users/{}/todos".format(
        url, employee_id)).json()

    for todo in todo_list:
        task = {}
        task["task"] = todo.get("title")
        task["completed"] = todo.get("completed")
        task["username"] = user.get("username")
        tasks.append(task)
    content[employee_id] = tasks

    with open(file_name, "w") as f:
        json.dump(content, f)
