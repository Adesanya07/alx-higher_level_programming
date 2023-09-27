#!/usr/bin/python3


import requests
import json

EMPLOYEE_ID = 1

response = requests.get(f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}')
employee = json.loads(response.text)

response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}')
todos = json.loads(response.text)

done_count = len([todo for todo in todos if todo['completed']])
total_count = len(todos)

print(f"Employee {employee['name']} is done with tasks ({done_count}/{total_count}):")

for todo in todos:
  if todo['completed']:
    print("\t"+ todo['title'])

