
names = ["Bread", "Milk", "Eggs", "Butter"]
prices = [40, 60, 120, 50]
stocks = [10, 5, 0, 8]

cart_items = []
cart_totals = []

# 2. Basic Inputs
cust_name = input("Enter Name: ")
dist = float(input("Distance (km): "))

# 3. Delivery Calculation
if dist <= 15:
    fee = 50
elif dist <= 30:
    fee = 100
else:
    print("Outside delivery zone!")
    exit()

# 4. Shopping Loop
while True:
    print("\nItems Available:")
    for i in range(len(names)):
        print(f"{i}. {names[i]} | Rs.{prices[i]} | Stock: {stocks[i]}")
    
    cmd = input("\nEnter Item No to buy (or 'x' to bill): ")
    if cmd.lower() == 'x':
        break
    
    idx = int(cmd)
    
    # Validation
    if stocks[idx] <= 0:
        print("OUT OF STOCK!")
        continue
        
    qty = int(input(f"Qty for {names[idx]}: "))
    
    if qty <= stocks[idx]:
        stocks[idx] -= qty  # Update stock
        line_total = qty * prices[idx]
        
        # Save to cart lists
        cart_items.append(f"{names[idx]} (x{qty})")
        cart_totals.append(line_total)
        print("Added to cart.")
    else:
        print("Error: Not enough stock!")

# 5. Final Bill
print(f"\n--- INVOICE: {cust_name} ---")
for i in range(len(cart_items)):
    print(f"{cart_items[i]}: Rs.{cart_totals[i]}")

subtotal = sum(cart_totals)
print(f"Delivery Fee: Rs.{fee}")
print(f"GRAND TOTAL: Rs.{subtotal + fee}")
