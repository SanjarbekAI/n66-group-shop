from core.database_settings import execute_query


def add_product():
    name = input("Enter product name: ")
    category_id = int(input("Enter category id: "))
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))

    query = """
            INSERT INTO products (name, category_id, quantity, price)
            VALUES (%s, %s, %s, %s);
        """
    params = (name, category_id, quantity, price)
    execute_query(query=query, params=params)

def show_products():
    query = """
        SELECT 
            p.id, 
            p.name, 
            c.name AS category_name, 
            p.quantity, 
            p.price, 
            p.added_at
        FROM products p
        LEFT JOIN categories c ON p.category_id = c.id
        ORDER BY p.id;
    """
    products = execute_query(query=query, fetch="all")

    if not products:
        print("📦 Mahsulotlar mavjud emas.")
        return

    print("\nMahsulotlar ro'yxati:")
    print("-" * 70)
    print(f"{'ID':<5} {'Nomi':<20} {'Kategoriya':<15} {'Soni':<7} {'Narxi':<10} {'Qo‘shilgan':<20}")
    print("-" * 70)

    for row in products:
        product_id, name, category, quantity, price, added_at = row
        print(f"{product_id:<5} {name:<20} {category or 'Nomaʼlum':<15} {quantity:<7} {price:<10} {added_at}")


def delete_product():
    try:
        product_id = int(input("O'chiriladigan mahsulot ID sini kiriting: "))
    except ValueError:
        print("Noto'g'ri ID kiritildi")
        return

    check_query = "SELECT * FROM products WHERE id = %s;"
    existing = execute_query(query=check_query, params=(product_id,), fetch="one")

    if not existing:
        print(f"ID {product_id} ga mos mahsulot topilmadi")
        return

    delete_query = "DELETE FROM products WHERE id = %s;"
    execute_query(query=delete_query, params=(product_id,))
    print(f"Mahsulot ID {product_id} muvaffaqiyatli o‘chirildi.")