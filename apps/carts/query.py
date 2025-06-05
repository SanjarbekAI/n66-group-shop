from core.database_settings import execute_query


cart = {}

def add_to_cart(product_id, quantity):
    result = execute_query("SELECT quantity FROM products WHERE product_id=%s", (product_id,))

    if not result:
        print("No such product found.")
        return

    available_quantity = result[0][0]

    if available_quantity >= quantity:
        cart[product_id] = quantity
        print(f"Added {quantity} of {product_id} to cart.")
    else:
        print(f"there is no enough quantity. Only {available_quantity} of {product_id} available.")

def view_cart():
    if not cart:
        print("cart is empty")
        return

    for product_id, quantity in cart.items():
        result = execute_query("SELECT name, price FROM products WHERE product_id = %s", (product_id,))
        if result:
            name, price = result[0]
            total = price * quantity
            print(f"{name} — {quantity} piece  — {price} $ — total: {total}$ ")
        else:
            print(f"{product_id} — product not found.")