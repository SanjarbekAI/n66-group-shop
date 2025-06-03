from apps.utils.execute_tables import execute_table_queries


def auth_menu():
    "Gavhar"


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
        auth_menu()
    else:
        print("Invalide choice !!!")
        user_menu()




def admin_menu():
    "Ulug'bek"
    print("""
    1. Add category
    2. Add product
    3. See products
    4. Delete product
    5. See orders
    6. Log out
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
            return auth_menu()
        else:
            print("Invalid choice!")
    except KeyboardInterrupt:
        print("Good bye")
    return admin_menu()


if __name__ == '__main__':
    execute_table_queries()
    auth_menu()
