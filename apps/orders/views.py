from core.database_settings import execute_query

def show_my_orders():
    id_query = """SELECT id FROM users WHERE is_login = TRUE;"""
    user_id = execute_query(query=id_query)
    print(user_id)
    list_query = """SELECT i.product_id, i.price, i.quantity FROM order_item as i INNER JOIN orders as o on o.id = i.order_id;"""
    orders_list = execute_query(query=list_query, params=(user_id,), fetch="all")

    if not orders_list:
        print("Buyurtma mavjud emas!")
        
    else:
        for order in orders_list:
            print(order)