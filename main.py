import os
from modules.listItems import listItems
def menu():
    print("1. List")
    print("2. Create")
    print("3. Edit")
    print("4. Delete")
    print("5. Exit")
    option = input("Choose an option: ")
    if option == "1":
        listItems()
        menu()
    elif option == "2":
        print("Creating...")
    elif option == "3":
        print("Editing...")
    elif option == "4":
        print("Deleting...")
    elif option == "5":
        print("Exiting...")
    else:
        print("Invalid option")

if __name__ == "__main__":
    # if not file style.css
    if not os.path.isfile("style.css"):
        print("style.css not found")
        exit()
    menu()
