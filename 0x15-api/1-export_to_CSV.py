#!/usr/bin/python3
"""
extend python script export data in the CSV format
"""
import csv
import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python todo_export.py [employee_id]")
    sys.exit(1)

employee_id = sys.argv[1]

response = requests.get(
    f"https://jsonplaceholder.typicode.com\
        /users/{employee_id}"
)
if response.status_code != 200:
    print("Error: Could not fetch data for the employee with ID", employee_id)
    sys.exit(1)

employee = response.json()
employee_name = employee["name"]

response = requests.get(
    f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
)
if response.status_code != 200:
    print(
        "Error: Could not fetch TODO list for \
            the employee with ID",
        employee_id,
    )
    sys.exit(1)

todos = response.json()

completed_tasks = [todo for todo in todos if todo["completed"]]
completed_task_count = len(completed_tasks)
total_task_count = len(todos)
print(
    f"Employee {employee_name} is done with\
    tasks({completed_task_count}/{total_task_count}):"
)
for todo in completed_tasks:
    print(f"\t{todo['title']}")
filename = f"{employee_id}.csv"
with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            )
    for todo in todos:
        writer.writerow(
                [employee_id, employee_name, todo["completed"], todo["title"]]
                )

print(f"Exported data to {filename}")
