from database import handler


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
    def find(name: str):
        return handler.find(Nation.TABLE, name)

    def extract(self):
        return {
            "name": self.name,
            "ip": self.ip,
        }

    def save(self):
        return handler.store(Nation.TABLE, self.extract())
