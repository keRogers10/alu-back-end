#!/usr/bin/py thon3
"""Get TODO list progress for a given employee ID."""

import json
import requests
import sys

def get_todo_progress(employee_id):
    # Fetch user information
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = json.loads(user_response.text)

    # Fetch TODO list for the employee
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_data = json.loads(todos_response.text)

    # Calculate the number of completed tasks and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    # Print the progress
    print(f"Employee {user_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_progress(employee_id)
