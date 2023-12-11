import json
from termcolor import colored

from models.user import User


class Nation:
    FILE = "database/nations.json"
    DATA = None

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.tag = kwargs.get("tag")

    def __str__(self):
        return f"- Tag: {self.tag}\t Name: {self.name}"

    @classmethod
    def read(cls):
        try:
            with open(Nation.FILE, "r") as db:
                nations = json.load(db)["nations"]
                Nation.DATA = [cls(**nation) for nation in nations]
        except:
            Nation.DATA = list()

    @classmethod
    def write(cls):
        with open(Nation.FILE, "w") as db:
            nations = [nation.extract() for nation in Nation.DATA]
            db.write(json.dumps({"nations": nations}))

    @classmethod
    def get(cls):
        """
        get list of Nation objects
        """
        return Nation.DATA

    @classmethod
    def find(cls, name: str):
        """
        get specific Nation object
        """
        for nation in Nation.DATA:
            if nation.name == name:
                return nation
        return None

    def save(self):
        Nation.DATA.append(self)
        Nation.write()

    def users(self):
        return User.get(nation=self.name)

    def extract(self):
        return {"name": self.name, "tag": self.tag}
