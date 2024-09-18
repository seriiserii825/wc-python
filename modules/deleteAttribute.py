import json
import subprocess
from libs.select import selectMultiple
from libs.selectWithFzf import selectWithFzf
from modules.getUser import getUser
from modules.listAttributes import listAttributes
from modules.showAttributes import showAttributes


def deleteAttribute():
    user = getUser()
    attributes = listAttributes()
    choice = input("Delete children attribute? (y/n): ")
    if choice == "y":
        attr_id_name = []
        for attribute in attributes:
            attr_id_name.append(f"{attribute['id']}. {attribute['name']}")
        parent_attribute = selectWithFzf(attr_id_name)
        parent_attribute_id = parent_attribute.split(".")[0]
        command = f"wp wc product_attribute_term list {parent_attribute_id} --user={user} --format=json"
        attribute_items = subprocess.check_output(command, shell=True, text=True)
        attribute_arr = json.loads(attribute_items)
        attribute_choose = []
        for item in attribute_arr:
            attribute_choose.append(f"{item['id']}. {item['name']}")
        choice = selectMultiple(attribute_choose)
        for item in choice:
            item_id = item.split(".")[0]
            command = f"wp wc product_attribute_term delete {parent_attribute_id} {item_id} --force=true --user={user}"
            subprocess.run(command, shell=True)
    else:
        print(f"attributes: {attributes}")
        attribute_to_choose = []
        for attribute in attributes:
            attribute_to_choose.append(f"{attribute['id']}. {attribute['name']}")
        attribute_choose = selectMultiple(attribute_to_choose)
        for item in attribute_choose:
            item_id = item.split(".")[0]
            command = f"wp wc product_attribute delete {item_id} --force=true --user={user}"
            subprocess.run(command, shell=True)
    showAttributes()

