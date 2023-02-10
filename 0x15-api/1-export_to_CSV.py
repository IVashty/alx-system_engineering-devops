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
    file_name = "{}.csv".format(employee_id)
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todo_list = requests.get("{}/users/{}/todos".format(url, employee_id)).json()

    with open(file_name, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            writer.writerow(
                [
                    employee_id,
                    user.get("username"),
                    todo.get("completed"),
                    todo.get("title"),
                ]
            )
