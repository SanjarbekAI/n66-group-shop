import psycopg2

def create_category_table():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
    """
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    print("Categories table created.")

def create_product_table():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(150) NOT NULL,
            category_id INTEGER REFERENCES categories(id),
            quantity INTEGER NOT NULL,
            price NUMERIC(10,2) NOT NULL,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    print("Products table created.")


create_category_table()
create_product_table()
