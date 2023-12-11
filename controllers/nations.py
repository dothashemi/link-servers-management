from termcolor import colored

from models.nation import Nation
from models.nation import User


class NationController:
    Nation.read()

    def __init__():
        pass

    @staticmethod
    def index():
        return Nation.get()

    @classmethod
    def create(cls, **kwargs):
        nation = Nation(**{"name": kwargs.get("name"), "tag": kwargs.get("tag")})
        nation.save()

        return nation

    @classmethod
    def show(cls, name):
        nation = Nation.find(name)
        users = nation.users() if nation is not None else None

        return nation, users
