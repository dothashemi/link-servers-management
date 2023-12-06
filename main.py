from users import User
from nations import Nation


def bprint(data: list):
    for item in data:
        for key in item.keys():
            print(f"{key}: {item[key]}")
        print()


if __name__ == "__main__":
    print("----- LINK SERVERS MANAGEMENT -----")
    print("-- 1. Nations")
    print("-- 2. Users")

    first = int(input("Enter: "))
    if first == 1:
        print("----- NATIONS -----")
        print("-- 1. Index")
        print("-- 2. Create")
        print("-- 3. Show Users")

        second = int(input("Enter: "))

        if second == 1:
            print("----- ALL NATIONS -----")
            bprint(Nation.all())

        elif second == 2:
            print("----- CREATE NATION -----")
            name = input("Name: ")
            ip = input("IP: ")
            print(Nation.create(name, ip))

        elif second == 3:
            print("----- SHOW NATION'S USERS -----")
            char = input("Nation: ")
            users = Nation.users(char)
            bprint(users)

    elif first == 2:
        print("----- USERS -----")
        print("-- 1. Index")
        print("-- 2. Find")
        print("-- 3. Create")

        second = int(input("Enter: "))

        if second == 1:
            print("----- ALL USERS -----")
            bprint(User.all())

        elif second == 3:
            print("----- CREATE USER -----")
            nation = input("Nation: ")
            name = input("Name: ")
            password = input("Password: ")
            onlines = int(input("Online Users: "))
            price = int(input("Price: "))
            tag = input("Tag: ")
            start = input("Start Date: ")
            User(nation, name, password, onlines, price, tag, start).save()
