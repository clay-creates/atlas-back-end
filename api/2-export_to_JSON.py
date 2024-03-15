#!/usr/bin/python3
""" Script using REST API """
import json
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
    username = employee_info.get('username')
    todo_list = requests.get(f"{todo_ext}?userId={employee_id}").json()

    # Prepare data for JSON
    todo_data =[]
    for item in todo_list:
        todo_data.append({
            "task": item["title"],
            "completed": item["completed"],
            "username": username
        })

    # Prepare JSON srtucture
    json_data = {str(employee_id): todo_data}

    # Write json_data to .json
    with open(f"{employee_id}.json", mode='w') as file:
        json.dump(json_data, file, indent=4)


if __name__ == "__main__":
    employee_todo(int(sys.argv[1]))
