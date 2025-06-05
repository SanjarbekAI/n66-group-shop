from core.database_settings import execute_query


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    full_name = input("Enter full name: ")

    check_query = "SELECT * FROM users WHERE username = %s;"
    existing = execute_query(query=check_query, params=(username,), fetch="one")
    if existing:
        print("Username already exists!")
        return

    insert_query = """
        INSERT INTO users (username, password, email, full_name)
        VALUES (%s, %s, %s, %s);
    """
    execute_query(query=insert_query, params=(username, password, email, full_name))
    print("Registration successful!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    query = "SELECT id FROM users WHERE username = %s AND password = %s;"
    user = execute_query(query=query, params=(username, password), fetch="one")

    if user:
        user_id = user[0]
        update_query = "UPDATE users SET is_login = TRUE WHERE id = %s;"
        execute_query(query=update_query, params=(user_id,))
        print("Login successful!")
        return user_id
    else:
        print("Invalid credentials!")
        return None


def logout(user_id):
    if user_id:
        update_query = "UPDATE users SET is_login = FALSE WHERE id = %s;"
        execute_query(query=update_query, params=(user_id,))
        print("Logout successful!")
    else:
        print("No user is currently logged in.")
