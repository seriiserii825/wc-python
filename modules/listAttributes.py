import json
import subprocess
from modules.getUser import getUser


def listAttributes():
    user = getUser()
    command=f"wp wc product_attribute list --user={user} --format=json"
    attributes = subprocess.check_output(command, shell=True, text=True)
    return json.loads(attributes)
