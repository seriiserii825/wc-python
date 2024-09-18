import subprocess
from libs.selectWithFzf import selectWithFzf
from modules.getUser import getUser
from modules.listAttributes import listAttributes
from modules.showAttributes import showAttributes


def createAttribute():
    user = getUser()
    attributes = listAttributes()
    choice = input("Create children attribute? (y/n): ")
    if choice == "y":
        attr_id_name = []
        for attribute in attributes:
            attr_id_name.append(f"{attribute['id']}. {attribute['name']}")
        parent_attribute = selectWithFzf(attr_id_name)
        parent_attribute_id = parent_attribute.split(".")[0]
        attribute_items = input("Enter the attribute items separated by comma: ")
        attribute_items = attribute_items.split(",")
        for item in attribute_items:
            item = f"{item}"
            command = f"wp wc product_attribute_term create {parent_attribute_id} --name={item} --user={user}"
            subprocess.run(command, shell=True)
    else:
        attribute_items = input("Enter the attribute items separated by comma: ")
        attribute_items = attribute_items.split(",")
        for item in attribute_items:
            item = f"{item}"
            command = f"wp wc product_attribute create --name={item} --user={user}"
            subprocess.run(command, shell=True)
    showAttributes()

