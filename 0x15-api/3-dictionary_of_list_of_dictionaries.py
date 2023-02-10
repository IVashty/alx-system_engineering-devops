#!/usr/bin/python3
"""
script returns a json about todo list of users
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users/".format(url)).json()
    content = {}
    for user in users:
        tasks = []
        employee_id = user.get("id")
        todo_list = requests.get("{}/users/{}/todos".format(
            url, employee_id)).json()
        for todo in todo_list:
            task = {}
            task["username"] = user.get("username")
            task["task"] = todo.get("title")
            task["completed"] = todo.get("completed")
            tasks.append(task)
        content[employee_id] = tasks
    with open("todo_all_employees.json", "w") as f:
        json.dump(content, f)
