import json
from os import path
import os


def _home_dir():
    return os.getenv('BDDTTER_STORAGE', '/Users/myszon/Projects/BDDWorkshop/.storage')


def store(filename, data):
    with open(f'{_home_dir()}/{filename}', 'w') as outfile:
        json.dump(data, outfile)


def load(filename):
    if path.exists(f'{_home_dir()}/{filename}'):
        with open(f'{_home_dir()}/{filename}') as json_file:
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