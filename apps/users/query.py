from core.database_settings import execute_query


def create_user_table():
    users = """
            CREATE TABLE IF NOT EXISTS users
            (
                id         SERIAL PRIMARY KEY,
                username   VARCHAR(50) NOT NULL,
                password   VARCHAR(50) NOT NULL,
                email      VARCHAR(50) NOT NULL,
                is_login   BOOLEAN   DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                full_name  VARCHAR(50) NOT NULL
            );
            """
    execute_query(query=users)
