

import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="praveen93",
    database="grocery_shop"
)

cursor = db.cursor()

cart_items = []
cart_totals = []

# Customer input
cust_name = input("Enter Name: ")
dist = float(input("Distance (km): "))

# Delivery fee
if dist <= 15:
    fee = 50
elif dist <= 30:
    fee = 100
else:
    print("Outside delivery zone!")
    exit()

while True:

    # Fetch products from DB
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("\nItems Available:")
    for p in products:
        print(f"{p[0]}. {p[1]} | Rs.{p[2]} | Stock: {p[3]}")

    cmd = input("\nEnter Item No to buy (or 'x' to bill): ")
    if cmd.lower() == 'x':
        break

    idx = int(cmd)

    cursor.execute("SELECT name, price, stock FROM products WHERE id=%s", (idx,))
    item = cursor.fetchone()

    name, price, stock = item

    if stock <= 0:
        print("OUT OF STOCK!")
        continue

    qty = int(input(f"Qty for {name}: "))

    if qty <= stock:
        new_stock = stock - qty
        total = qty * price

        # Update stock
        cursor.execute(
            "UPDATE products SET stock=%s WHERE id=%s",
            (new_stock, idx)
        )

        # Save order
        cursor.execute(
            "INSERT INTO orders (customer_name, item_name, quantity, total) VALUES (%s,%s,%s,%s)",
            (cust_name, name, qty, total)
        )

        db.commit()

        cart_items.append(f"{name} (x{qty})")
        cart_totals.append(total)

        print("Added to cart.")

    else:
        print("Error: Not enough stock!")

# Final bill
print(f"\n--- INVOICE: {cust_name} ---")

for i in range(len(cart_items)):
    print(f"{cart_items[i]}: Rs.{cart_totals[i]}")

subtotal = sum(cart_totals)

print(f"Delivery Fee: Rs.{fee}")
print(f"GRAND TOTAL: Rs.{subtotal + fee}")

db.close()
