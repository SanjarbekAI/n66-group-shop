from apps.orders.query import create_order_table, create_order_item_table
from apps.products.query import create_category_table, create_product_table
from apps.users.query import create_user_table


def execute_table_queries():
    create_user_table()
    create_category_table()
    create_product_table()
    create_order_table()
    create_order_item_table()
