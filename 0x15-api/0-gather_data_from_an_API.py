#!/usr/bin/python3
"""
script gathers data from an API  to return information about\
        employee todo list progess
requests module
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Get information about an employee's TODO list progress

    Args:
        employee_id (int): ID of the employee

    Returns:
        None
    """
    # Base URL for the REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get information about the employee
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee = employee_response.json()
    employee_name = employee["name"]

    # Get the employee's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_list = todo_response.json()

    # Count the number of completed and total tasks
    completed_tasks = [task for task in todo_list if task["completed"] is True]
    total_tasks = len(todo_list)
    completed_tasks_count = len(completed_tasks)

    # Display the employee's TODO list progress
    print(
        f"Employee {employee_name} is done\
                with tasks({completed_tasks_count}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f'\t{task["title"]}')


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print(
            "Error: Please provide an employee\
                ID as a command-line argument."
        )
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
