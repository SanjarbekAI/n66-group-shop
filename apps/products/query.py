from core.database_settings import execute_query
from core.config import get_connection


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

def show_products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT id, name, category_id, quantity, price, added_at FROM products ORDER BY id;
    """)
    rows = cur.fetchall()
    print("List of products!")
    if not rows:
        print("Products not found!")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Category ID: {row[2]} | Quantity {row[3]} | Price: {row[4]} | Date of added: {row[5]}")
    cur.close()
    conn.close()


