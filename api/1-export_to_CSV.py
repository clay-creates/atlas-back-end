#!/usr/bin/usr/python3
""" Script using REST API """
import csv
import requests
import sys


def employee_todo(employee_id):
    """ Function works with employee todo's, shows total todo and completed"""
    site_url = "https://jsonplaceholder.typicode.com/"
    employee_ext = f"{site_url}/users/{employee_id}"
    todo_ext = f"{site_url}/todos"

    employee_info = requests.get(employee_ext).json()
    employee_name = employee_info['name']
    todo_list = requests.get(todo_ext, params={"userId": employee_id}).json()

    csv_data = [['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']]
    for item in todo_list:
        csv_data.append([employee_id, employee_name, item["completed"], item["title"]])



    # completed_todos = []
    # for item in todo_list:
    #     if item["completed"]:
    #         completed_todos.append(item["title"])

    # total_todo = len(todo_list)
    # total_done = len(completed_todos)

    # print ("Employee {0} is done with tasks({1}/{2}):"
    #        .format(employee_name, total_done, total_todo))
    # for todo in completed_todos:
    #     print(f"\t {todo}")

if __name__ == "__main__":
    employee_todo(int(sys.argv[1]))
