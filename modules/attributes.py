from modules.createAttribute import createAttribute
from modules.showAttributes import showAttributes


def attributes():
    print("1. List")
    print("2. Create")
    print("3. Edit")
    print("4. Delete")
    print("5. Back")
    option = input("Choose an option: ")
    if option == "1":
        showAttributes()
    elif option == "2":
        createAttribute()
    elif option == "3":
        print("Editing...")
    elif option == "4":
        print("Deleting...")
    elif option == "5":
        return
    else:
        print("Invalid option")
