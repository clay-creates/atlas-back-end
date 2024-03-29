#!/usr/bin/python3
""" Script using REST API """
import requests
import sys


def employee_todo(employee_id):
    """ Function works with employee todo's, shows total todo and completed"""
    # Set up API connection
    site_url = "https://jsonplaceholder.typicode.com/"
    employee_ext = f"{site_url}/users/{employee_id}"
    todo_ext = f"{site_url}/todos"

    # Get request from API
    employee_info = requests.get(employee_ext).json()
    employee_name = employee_info.get('name')
    todo_list = requests.get(f"{todo_ext}?userId={employee_id}").json()

    # Create list of completed to-do's
    completed_todos = []
    for item in todo_list:
        if item["completed"]:
            completed_todos.append(item["title"])

    # Count totals
    total_todo = len(todo_list)
    total_done = len(completed_todos)

    # Print results
    print("Employee {0} is done with tasks({1}/{2}):"
          .format(employee_name, total_done, total_todo))
    for todo in completed_todos:
        print(f"\t {todo}")


if __name__ == "__main__":
    employee_todo(int(sys.argv[1]))
