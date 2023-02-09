#!/usr/bin/python3
"""
This script exports data from a REST API to a CSV file.

The REST API provides information about the \
        TODO list progress of employees, given their ID.
The exported CSV file contains the following information \
        for each task owned by the employee:
    USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE

The file name is formatted as USER_ID.csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_tasks = []
    employee_name = ""

    # Get the employee information and tasks
    url = "https://jsonplaceholder.typicode.com/users/{}"
    user_url = url.format(employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )
    user_res = requests.get(user_url)
    tasks_res = requests.get(tasks_url)

    if user_res.status_code == 200:
        employee_name = user_res.json().get("name")
    if tasks_res.status_code == 200:
        tasks = tasks_res.json()
        for task in tasks:
            task_info = [
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title"),
            ]
            employee_tasks.append(task_info)

    # Export the data to a CSV file
    file_name = "{}.csv".format(employee_id)
    with open(file_name, mode="w") as file:
        writer = csv.writer(file)
        writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
            ])
        writer.writerows(employee_tasks)
