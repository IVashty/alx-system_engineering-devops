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
    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".\
        format(employee_id)
    response = requests.get(api_url)
    employee_todos = response.json()

    completed_tasks = [
            task for task in employee_todos
            if task.get("completed") is True
            ]
    username = response.json()[0].get("username")

    file_name = "{}.csv".format(employee_id)
    with open(file_name, mode="w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
            ])
        for task in completed_tasks:
            writer.writerow([employee_id, username, "True", task.get("title")])
