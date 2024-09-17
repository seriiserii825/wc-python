import os
def getUser():
    command = f"wp user list --field=name"
    user = os.system(command)
    return user
