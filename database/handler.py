import json

from database import decorators

BASE = "database"


@decorators.validation
def get(table: str):
    """
    get all data from json file
    """
    with open(f"{BASE}/{table}.json", "r") as db:
        return json.load(db)[table]


@decorators.validation
def first(table: str, name: str):
    """
    get one data from json file based on the name key
    """
    with open(f"{BASE}/{table}.json", "r") as db:
        data = json.load(db)[table]

        for item in data:
            if item["name"] == name:
                return item

    return None


@decorators.validation
def store(table: str, item: dict):
    """
    append new data to json file
    """
    tmp = get(table)
    all = tmp if tmp is not None else list()
    all.append(item)

    with open(f"{BASE}/{table}.json", "w") as db:
        db.write(json.dumps({table: all}))


def update(table: str):
    pass


def deactivate(table: str, name: str):
    pass
