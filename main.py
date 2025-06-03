from apps.utils.execute_tables import execute_table_queries


def auth_menu():
    "Gavhar"


def user_menu():
    "Javohir"


def admin_menu():
    "Ulug'bek"
    print("""
    1. Add category
    2. Add product
    3. Show products
    4. Delete product
    5. Show orders
    6. Change order status
    7. Log out
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
            return auth_menu()
        else:
            print("Invalid choice!")
    except KeyboardInterrupt:
        print("Good bye")
    return admin_menu()


if __name__ == '__main__':
    execute_table_queries()
    auth_menu()
