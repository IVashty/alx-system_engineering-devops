#!/usr/bin/python3
"""
script using REST API  to return information about
employee todo list progess
"""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python todo_list_progress.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = f"http://jsonplaceholder.typicode.com/users/{employee_id}"

response = requests.get(url)
if response.status_code != 200:
    print("Could not get information for employee with ID", employee_id)
    sys.exit(1)

employee_info = response.json()
employee_name = employee_info["name"]

url = f"http://jsonplaceholder.typicode.com/todos?userId={employee_id}"
response = requests.get(url)
if response.status_code != 200:
    print("Could not get todo list for employee with ID", employee_id)
    sys.exit(1)

todo_list = response.json()

completed_tasks = [task for task in todo_list if task["completed"]]
number_of_done_tasks = len(completed_tasks)
total_number_of_tasks = len(todo_list)

print(
    "Employee {employee_name} is done with tasks\
            ({number_of_done_tasks}/{total_number_of_tasks}):"
)
for task in completed_tasks:
    print("\t", task["title"])
