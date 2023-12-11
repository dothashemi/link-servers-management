import json


class User:
    FILE = "database/users.json"
    DATA = None

    def __init__(self, **kwargs):
        self.nation = kwargs.get("nation")
        self.name = kwargs.get("name")
        self.password = kwargs.get("password")
        self.onlines = kwargs.get("onlines")
        self.amount = kwargs.get("amount")
        self.reminder = kwargs.get("reminder")
        self.tag = kwargs.get("tag")
        self.status = kwargs.get("status")
        self.expire = kwargs.get("expire")

    def __str__(self):
        return f"+ Tag: {self.tag}\t Name: {self.name}\t Status: {self.status}\t Expire: {self.expire}"

    @classmethod
    def read(cls):
        try:
            with open(User.FILE, "r") as db:
                users = json.load(db)["users"]
                User.DATA = [cls(**user) for user in users]
        except:
            User.DATA = list()

        return User.DATA

    @classmethod
    def write(cls):
        with open(User.FILE, "w") as db:
            users = [user.extract() for user in User.DATA]
            db.write(json.dumps({"users": users}))

    @classmethod
    def get(cls, nation: str = None):
        """
        get list of User objects
        """
        if nation:
            return [user for user in User.DATA if user.nation == nation]

        return User.DATA

    @classmethod
    def find(cls, name: str):
        """
        get specific User object
        """
        for user in User.DATA:
            if user.name == name:
                return user
        return None

    def save(self):
        User.DATA.append(self)
        User.write()

    def extract(self):
        return {
            "nation": self.nation,
            "name": self.name,
            "password": self.password,
            "onlines": self.onlines,
            "amount": self.amount,
            "reminder": self.reminder,
            "tag": self.tag,
            "status": self.status,
            "expire": self.expire,
        }
