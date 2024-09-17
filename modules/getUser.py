import subprocess
def getUser():
    command = f"wp user list --field=user_login --role=administrator"
    user = subprocess.check_output(command, shell=True, text=True).strip()
    return user
