from modules.getUser import getUser


def listProducts():
    user = getUser()
    print(f"user: {user}")
