
from modules.showProducts import showProducts


def products():
    print("1. List")
    print("2. Create")
    print("3. Edit")
    print("4. Delete")
    print("5. Back")
    option = input("Choose an option: ")
    if option == "1":
        showProducts()
    elif option == "2":
        print("Creating...")
    elif option == "3":
        print("Editing...")
    elif option == "4":
        print("Deleting...")
    elif option == "5":
        return
    else:
        print("Invalid option")
