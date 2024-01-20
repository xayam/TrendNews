from utils import DEBUG


class Log:

    def __init__(self):
        pass

    @staticmethod
    def debug(message):
        if DEBUG:
            print(f"[MYDEBUG] {message}")
