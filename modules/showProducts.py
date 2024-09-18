from libs.richTable import richTable
from modules.listProducts import listProducts

def showProducts():
    products = listProducts()
    rows = []
    columns = ['id', 'name', 'slug', 'permalink', 'type', 'status', 'featured']
    for product in products:
        row = []
        for column in columns:
            row.append("".join(str(product[column])))
        rows.append(row)

    # print(f"rows: {rows}")
    title = "List of Products"
    richTable(title, columns, rows)

