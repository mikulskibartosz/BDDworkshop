import requests


URL = 'http://0.0.0.0:5000/tasks'

def get_tasks():
    response = requests.get(URL)
    return response.json()

def add_task(task):
    requests.post(URL, json=task)

def complete_task(task_id):
    requests.put(f'{URL}/completed/{task_id}')

