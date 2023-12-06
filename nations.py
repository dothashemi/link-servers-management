from termcolor import colored

from database import handler
from users import User


class Nation:
    TABLE = "nations"

    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def __str__(self):
        return self.name

    @staticmethod
    def all():
        return handler.get(Nation.TABLE)

    @staticmethod
    def users(name: str):
        users = User.all()
        return [user for user in users if user["nation"] == name]

    @staticmethod
    def find(name: str):
        return handler.first(Nation.TABLE, name)

    @classmethod
    def create(cls, name, ip):
        if cls.find(name):
            return colored("ERROR: nation exists!", "red")

        cls(name, ip).save()
        return colored(f"{name} nation created!", "green")

    def extract(self):
        return {
            "name": self.name,
            "ip": self.ip,
        }

    def save(self):
        return handler.store(Nation.TABLE, self.extract())
