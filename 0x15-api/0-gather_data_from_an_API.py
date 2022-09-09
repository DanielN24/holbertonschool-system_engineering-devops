#!/usr/bin/python3
"""
using this REST API, for a given employee ID
returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":

    employee_id = argv[1]
    rest_api_users = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    restapi_all = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)

    req_users = requests.get(rest_api_users).json()
    todos = requests.get(restapi_all).json()

    EMPLOYEE_NAME = req_users['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    tasks = []

    for task in todos:
        if task['completed'] is True:
            tasks.append(task['title'])
    print("Employee {} is done with tasks({}/{}): ".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in tasks:
        print("\t {}".format(task))
