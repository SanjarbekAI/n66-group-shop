from core.database_settings import execute_query

def show_my_orders():
    id_query = """SELECT id FROM users WHERE is_login = TRUE;"""
    res = execute_query(query=id_query)
    user_id = res
    list_query = """SELECT * FROM order_items WHERE order_id = %s;"""
    orders_list = execute_query(query=list_query, params=(user_id,), fetch="all")

    if not orders_list:
        print("Buyurtma mavjud emas!")
        
    else:
        for order in orders_list:
            print(order)