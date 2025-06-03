from core.database_settings import execute_query


def create_category_table():
    query = """
            CREATE TABLE IF NOT EXISTS categories
            (
                id   SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            );
            """
    execute_query(query=query)


def create_product_table():
    query = """
            CREATE TABLE IF NOT EXISTS products
            (
                id          SERIAL PRIMARY KEY,
                name        VARCHAR(150)   NOT NULL,
                category_id INTEGER REFERENCES categories (id),
                quantity    INTEGER        NOT NULL,
                price       NUMERIC(10, 2) NOT NULL,
                added_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
    execute_query(query=query)
