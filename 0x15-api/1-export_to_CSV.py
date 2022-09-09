#!/usr/bin/python3
"""
using this REST API, for a given employee ID
returns information about his/her TODO list progress
"""
import csv
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
    username = req_users['username']
    complete = todos[1]['completed']
    title = todos[1]['title']

    with open('USER_ID.csv', mode='w') as csv_file:
        user_writer = csv.writer(
            csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for tasks in todos:
            user_writer.writerow(
                ['"{}"'.format(tasks['userId']), '"{}"'.format(username),
                 '"{}"'.format(tasks['completed']), '"{}"'.format(
                        tasks['title'])])
