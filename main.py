from random import choice

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


if __name__ == '__main__':
    execute_table_queries()
    auth_menu()
