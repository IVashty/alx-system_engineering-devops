#!/usr/bin/python3
"""
export data in jason format but all in the records
"""

import requests
import json

# Get all tasks from the API
response = requests.get("https://jsonplaceholder.typicode.com/todos")
tasks = response.json()

# Group tasks by user id
grouped_tasks = {}
for task in tasks:
    if task["userId"] not in grouped_tasks:
        grouped_tasks[task["userId"]] = []
    grouped_tasks[task["userId"]].append(
        {
            "username": task["userId"],
            "task": task["title"],
            "completed": task["completed"],
        }
    )

# Save the grouped tasks to a JSON file
with open("todo_all_employees.json", "w") as file:
    json.dump(grouped_tasks, file)
