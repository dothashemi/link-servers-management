def validation(func):
    def wrapper(*args, **kwargs):
        table = args[0]
        if table not in ("nations", "users"):
            return None

        return func(*args, **kwargs)

    return wrapper
