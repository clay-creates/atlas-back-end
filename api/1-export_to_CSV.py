#!/usr/bin/python3
""" Script using REST API """
import csv
import requests
import sys


def employee_todo(employee_id):
    """ Function works with employee todo's, shows total todo and completed"""
    # Establish connection to API
    site_url = "https://jsonplaceholder.typicode.com/"
    employee_ext = f"{site_url}/users/{employee_id}"
    todo_ext = f"{site_url}/todos"

    # Get request information from API
    employee_info = requests.get(employee_ext).json()
    employee_name = employee_info.get('name')
    todo_list = requests.get(f"{todo_ext}?userId={employee_id}").json()

    # Prepare data for csv [[List of Lists]]
    csv_data = [['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']]
    for item in todo_list:
        csv_data.append([employee_id, employee_name, item["completed"], item["title"]])

    # Write csv_data to .csv file
    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print(f"Data for employee {employee_id} has been exported to {employee_id}.csv")


if __name__ == "__main__":
    employee_todo(int(sys.argv[1]))
