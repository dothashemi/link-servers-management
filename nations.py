from database import handler


TABLE = "nations"


def index():
    return handler.get(TABLE)


def create():
    name = input("Enter Name: ")
    ip = input("Enter Current IP: ")

    return handler.store(TABLE, {"name": name, "ip": ip})


def show(name: str):
    return handler.first(TABLE, name)


def find(name: str):
    print(f"### {handler.first(TABLE, name)}")
    return True if handler.first(TABLE, name) else False
