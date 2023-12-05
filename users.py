from datetime import datetime
import nations

from database import handler


TABLE = "users"


def show(name: str):
    return handler.first("users", name)


def create():
    nation = input("Enter Nation: ")
    name = input("Enter Name: ")
    password = input("Enter Password: ")
    type = input("Enter Type: ")
    users = int(input("Enter Online Users: "))
    price = int(input("Enter Price: "))
    tag = input("Enter Tag: ")
    start = input("Enter Start Date: ")

    if not nations.find(nation):
        print("Nation is Wrong!")
        return None

    return handler.store(
        TABLE,
        {
            "nation": nation,
            "name": name,
            "password": password,
            "type": type,
            "users": users,
            "price": price,
            "tag": tag,
            "start": start if start else datetime.now().strftime("%Y-%m-%d"),
        },
    )
