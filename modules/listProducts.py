import json
import subprocess
from libs.richTable import richTable
from modules.getUser import getUser


def listProducts():
    user = getUser()
    command=f"wp wc product list --user={user} --format=json"
    products = subprocess.check_output(command, shell=True, text=True)
    products = json.loads(products)
    rows = []
    columns = ['id', 'name', 'slug', 'permalink', 'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt', 'type', 'status', 'featured']
    print(f"columns: {columns}")
    for product in products:
        row = []
        for column in columns:
            row.append(product[column])
        rows.append(row)

    # print(f"rows: {rows}")
    title = "List of Products"
    richTable(title, columns, rows)


