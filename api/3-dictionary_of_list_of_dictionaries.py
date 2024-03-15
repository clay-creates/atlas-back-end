#!/usr/bin/python3
""" Script using REST API """
import json
import requests


def fetch_all_employees():
    """ Fetches all employees from API """
    # Set up API connection
    site_url = "https://jsonplaceholder.typicode.com/"
    employee_ext = f"{site_url}/users"

    # Return get request
    return requests.get(employee_ext).json()

def employee_todo(employee_id):
    """ Fetches employee todos from employee_id """
    # Set up API connection
    site_url = "https://jsonplaceholder.typicode.com/"
    employee_ext = f"{site_url}/users/{employee_id}"
    todo_ext = f"{site_url}/todos"

    # Get request from API
    employee_info = requests.get(employee_ext).json()
    username = employee_info.get('username')
    todo_list = requests.get(f"{todo_ext}?userId={employee_id}").json()

    # Prepare data for JSON
    todo_data = []
    for item in todo_list:
        todo_data.append({
            "task": item["title"],
            "completed": item["completed"],
            "username": username
        })

    # Return JSON structure
    return {str(employee_id): todo_data}

def export_to_json(data):
    """ Exports data to a JSON file """
    # Write json_data to .json
    with open(f"todo_all_employees.json", mode='w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    all_employees = fetch_all_employees()
    all_data = {}
    for employee in all_employees:
        employee_id = employee['id']
        all_data.update(employee_todo(employee_id))
    export_to_json(all_data)
