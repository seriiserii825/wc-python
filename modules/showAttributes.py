import json
import os
import subprocess
from libs.richTable import richTable
from modules.getUser import getUser
from modules.listAttributes import listAttributes

def showAttributes():
    user = getUser()
    items = listAttributes()
    rows = []
    columns = ['id', 'name',  'children', 'slug', 'type', 'order_by', 'has_archives']
    for item in items:
        children_row = []
        children_command = f"wp wc product_attribute_term list {item['id']} --user={user} --format=json"
        children = os.system(children_command)
        if children == 0:
            children = subprocess.check_output(children_command, shell=True, text=True)
            children = json.loads(children)
            for child in children:
                children_row.append(child['name'])
        else:
            children_row.append("None")

        row = []
        for column in columns:
            if column == "children":
                # each child on new line
                row.append("\n".join(children_row))
            else:
                row.append("".join(str(item[column])))
        rows.append(row)

    title = "List of Attributes"
    richTable(title, columns, rows)

