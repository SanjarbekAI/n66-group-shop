from apps.products.query import show_products
from apps.products.views import add_product, delete_product
from apps.utils.execute_tables import execute_table_queries
from apps.users.views import register, login
from apps.orders.views import show_my_orders

current_user = None


def auth_menu():
    global current_user

    while True:
        print("\nWelcome to the authentication menu!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user == "admin":
                current_user = "admin"
                return admin_menu()
            elif user:
                current_user = user
                return user_menu()
            else:
                continue
        elif choice == '3':
            print("Exiting... Goodbye!")
            exit()
        else:
            print("Invalid choice. Try again.")



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
        show_my_orders()
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
            add_product()
        elif choice == "5":
            show_products()
        elif choice == "6":
            delete_product()
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
