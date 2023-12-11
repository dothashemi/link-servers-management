from models.user import User
from models.nation import Nation
from datetime import datetime, timedelta

# Get the current date

# Calculate the date 30 days from today


class UserController:
    User.read()

    def __init__():
        pass

    @classmethod
    def index(cls, nation: str = None):
        return User.get()

    @classmethod
    def create(cls, nation, name, password, onlines, tag, start, amount=0, reminder=0):
        if Nation.find(nation) is None:
            return None

        if User.find(name):
            return None

        if start == "":
            today = datetime.now()
            expire = (today + timedelta(days=30)).strftime("%Y-%m-%d")

        onlines = int(onlines)
        amount = int(amount)
        status = "active"

        user = User(
            nation=nation,
            name=name,
            password=password,
            onlines=onlines,
            amount=amount,
            reminder=reminder,
            tag=tag,
            status=status,
            expire=expire,
        )
        user.save()

        return user
