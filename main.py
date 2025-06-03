from apps.utils.execute_tables import execute_table_queries


def auth_menu():
    print("welcome to the authentication menu!")
    print(" 1 register")
    print(" 2 login")
    print(" 3 exit")
    choice= input("Please choose an option: ")
    if choice == '1':
        pass
        
        
    elif choice == '2':
        pass
 
    elif choice == '3':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice, please try again.")




def user_menu():
    "Javohir"


def admin_menu():
    "Ulug'bek"


if __name__ == '__main__':
    execute_table_queries()
    auth_menu()
