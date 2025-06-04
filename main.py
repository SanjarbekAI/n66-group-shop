from apps.products.query import show_products
from apps.utils.execute_tables import execute_table_queries


def auth_menu():
    print("welcome to the authentication menu!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Please choose an option: ")
    if choice == '1':
        pass

    elif choice == '2':
        pass

    elif choice == '3':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice, please try again.")
    return auth_menu()


def user_menu():
    print("""
    User_menu:
        1. View products
        2. Add to Cart
        3. View cart
        4. Ordering
        5. My orders
        6. Logout
    """)

    choice = input("Enter your choice: ")
    if choice == "1":
        show_products()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        auth_menu()
    else:
        print("Invalid choice !!!")
    user_menu()


def admin_menu():
    print("""
    1. Add category
    2. Show categories
    3. Delete category
    4. Add product
    5. Show products
    6. Delete product
    7. Show orders
    8. Change order status
    9. Log out
    """)

    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
            return auth_menu()
        else:
            print("Invalid choice!")
    except KeyboardInterrupt:
        print("Good bye")
    return admin_menu()


if __name__ == '__main__':
    execute_table_queries()
    auth_menu()
