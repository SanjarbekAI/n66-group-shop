def create_order_table():
    order_table_query = "CREATE TABLE IF NOT EXISTS orders(" \
    "id SERIAL PRIMARY KEY," \
    "user_id INTEGER REFERENCE clients(id)," \
    "order_date TIMESTAMP);"


def create_order_item():
    order_item_query = "CREATE TABLE IF NOT EXISTS order_items(" \
    "id SERIAL PRIMARY KEY," \
    "order_id INTEGER REFERENCE orders(id)," \
    "product_id INTEGER REFERENCE products(id)," \
    "quantity INTEGER);"
