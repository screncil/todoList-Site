from .models import Users
import time


def checkUser(username: str, password: str) -> bool:
    user = Users.objects.filter(username=username, password=password)
    return bool(len(user))

def addUser(username: str, password: bytes) -> bool:
    if not checkUser(username, password):
        try:
            user = Users(username=username, password=password, register_time=int(time.time()))
            user.save()
            return True
        except Exception:
            return False