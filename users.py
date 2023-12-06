from datetime import datetime

from database import handler


class User:
    TABLE = "users"

    def __init__(self, nation, name, password, onlines, price, tag, start):
        self.nation = nation
        self.name = name
        self.password = password
        self.onlines = onlines
        self.price = price
        self.tag = tag
        self.start = start

    def __str__(self):
        return self.name

    @staticmethod
    def all():
        return handler.get(User.TABLE)

    @staticmethod
    def find(name: str):
        return handler.find(User.TABLE, name)

    def extract(self):
        return {
            "nation": self.nation,
            "name": self.name,
            "password": self.password,
            "onlines": self.onlines,
            "price": self.price,
            "tag": self.tag,
            "start": self.start,
        }

    def save(self):
        return handler.store(User.TABLE, self.extract())
