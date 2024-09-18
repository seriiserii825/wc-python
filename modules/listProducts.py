import json
import subprocess
from modules.getUser import getUser


def listProducts():
    user = getUser()
    command=f"wp wc product list --user={user} --format=json"
    products = subprocess.check_output(command, shell=True, text=True)
    return json.loads(products)
