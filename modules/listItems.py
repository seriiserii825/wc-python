from modules.listProducts import listProducts


def listItems():
    print('Choose items to list:')
    print('1. Products')
    print('2. Attributes')
    print('3. Categories')
    print('4. Orders')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        listProducts()
    elif choice == '2':
        # listAttributes()
        print('Not implemented yet')
    elif choice == '3':
        # listCategories()
        print('Not implemented yet')
    elif choice == '4':
        # listOrders()
        print('Not implemented yet')
    elif choice == '5':
        return
    else:
        print('Invalid choice')

