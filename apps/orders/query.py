from core.database_settings import execute_query


def create_order_table():
    order = """
            CREATE TABLE IF NOT EXISTS orders
            (
                id         SERIAL PRIMARY KEY,
                user_id    INTEGER REFERENCES users (id),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
    execute_query(query=order)


def create_order_item_table():
    order_item = """
                 CREATE TABLE IF NOT EXISTS order_items
                 (
                     id         SERIAL PRIMARY KEY,
                     order_id   INTEGER REFERENCES orders (id),
                     product_id INTEGER REFERENCES products (id),
                     price      NUMERIC(10, 2) NOT NULL,
                     quantity   INTEGER        NOT NULL
                 );
                 """
    execute_query(query=order_item)
