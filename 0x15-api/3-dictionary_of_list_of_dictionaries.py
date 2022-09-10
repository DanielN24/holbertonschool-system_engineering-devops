#!/usr/bin/python3
"""
 Python script to export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":

    rest_api_users = "https://jsonplaceholder.typicode.com/users"
    req_users = requests.get(rest_api_users).json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(rest_api_users + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in req_users}, jsonfile)
