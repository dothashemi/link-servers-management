import users
import nations


if __name__ == "__main__":
    print("----- LINK SERVERS MANAGEMENT -----")
    print("-- 1. Nations")
    print("-- 2. Users")

    first = int(input("Enter: "))
    if first == 1:
        print("----- NATIONS -----")
        print("-- 1. Index")
        print("-- 2. Show")
        print("-- 3. Create")

        second = int(input("Enter: "))
        if second == 3:
            print("----- CREATE NATION -----")
            nations.create()

    elif first == 2:
        print("----- USERS -----")
        print("-- 1. Index")
        print("-- 2. Show")
        print("-- 3. Create")

        second = int(input("Enter: "))
        if second == 3:
            print("----- CREATE USER -----")
            users.create()
