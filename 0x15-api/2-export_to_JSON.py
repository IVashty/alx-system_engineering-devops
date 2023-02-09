#!/usr/bin/python3
"""
This script retrieves information about \
        the tasks of an employee from a REST API
and exports the data in JSON format.
"""
import json
import sys
import requests

if __name__ == "__main__":
    # Get employee ID from the command line argument
    employee_id = sys.argv[1]

    # Make a GET request to the REST API
    url = "https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)

    # Get the JSON data from the response
    employee_data = response.json()
    employee_name = employee_data.get("name")

    # Make a GET request to the REST API to get the tasks of the employee
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    # Get the JSON data from the response
    tasks = response.json()

    # Store the data in a dictionary
    employee_tasks = {employee_id: []}
    for task in tasks:
        employee_tasks[employee_id].append(
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name,
            }
        )

    # Write the data to a JSON file
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(employee_tasks, json_file)
