import os

from controllers.nations import NationController
from controllers.users import UserController


def menu():
    os.system("clear")
    print("----- LINK SERVERS MANAGEMENT -----")
    print("-- 1. Nations")
    print("-- 2. Users")
    print()
    print("-- 0. Exit")

    first = int(input("Enter: "))
    os.system("clear")

    if first == 1:
        print("----- NATIONS -----")
        print("-- 1. Index")
        print("-- 2. Create")
        print("-- 3. Show")

        second = int(input("Enter: "))
        os.system("clear")

        if second == 1:
            print("----- ALL NATIONS -----")
            nations = NationController.index()
            for nation in nations:
                print(nation)

        elif second == 2:
            print("----- CREATE NATION -----")
            name = input("Name: ")
            tag = input("Tag: ")
            print(NationController.create(**{"name": name, "tag": tag}))

        elif second == 3:
            print("----- SHOW NATION -----")
            char = input("Nation: ")
            nation, users = NationController.show(char)
            print(nation)
            for user in users:
                print(user)

    elif first == 2:
        print("----- USERS -----")
        print("-- 1. Index")
        print("-- 2. Find")
        print("-- 3. Create")

        second = int(input("Enter: "))
        os.system("clear")

        if second == 1:
            print("----- ALL USERS -----")
            users = UserController.index()
            for user in users:
                print(user)

        elif second == 3:
            print("----- CREATE USER -----")
            nation = input("Nation: ")
            name = input("Name: ")
            password = input("Password: ")
            onlines = input("Online Users: ")
            amount = input("Amount: ")
            tag = input("Tag: ")
            start = input("Start Date: ")

            user = UserController.create(
                nation=nation,
                name=name,
                password=password,
                onlines=onlines,
                amount=amount,
                tag=tag,
                start=start,
            )

            print(user)


if __name__ == "__main__":
    menu()
