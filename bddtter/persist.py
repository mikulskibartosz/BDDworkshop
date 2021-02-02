import json
from os import path
import os

DIRECTORY = '/Users/myszon/Projects/BDDWorkshop/.storage'


def store(filename, data):
    with open(f'{DIRECTORY}/{filename}', 'w') as outfile:
        json.dump(data, outfile)


def load(filename):
    if path.exists(f'{DIRECTORY}/{filename}'):
        with open(f'{DIRECTORY}/{filename}') as json_file:
            return json.load(json_file)
    else:
        return []


class Persist:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.content = load(self.filename)
        return self.content

    def __exit__(self, exc_type, exc_val, exc_tb):
        store(self.filename, self.content)