#!/usr/bin/python3
"""
 Python script to export data in the JSON format.
"""
import json
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

    with open('{}.json'.format(argv[1]), 'w') as file:
        task_list = []
        for task in todos:
            edited_task = {"task": task['title'],
                           "completed": task['completed'],
                           "username": req_users['username']}
            task_list.append(edited_task)
        write_dict = {req_users['id']: task_list}
        file.write(json.dumps(write_dict))
