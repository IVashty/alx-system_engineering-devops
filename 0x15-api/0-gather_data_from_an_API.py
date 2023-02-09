#!/usr/bin/python3
"""
This script returns information about an \
        employee's TODO list progress from a REST API
"""
import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Get employee TODO list progress from REST API

    Returns:
        str: formatted string containing employee TODO list progress
    """
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)

    if response.status_code != 200:
        return "Employee not found"

    employee = response.json()
    employee_name = employee.get("name")
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    completed_todos = [todo.get("title")
                       for todo in todos
                       if todo.get("completed")
                       ]
    todo_count = len(todos)
    completed_count = len(completed_todos)

    result = "Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_count, todo_count
    )
    for todo in completed_todos:
        result += "\n\t {}".format(todo)

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    result = get_employee_todo_list(employee_id)
    print(result)
