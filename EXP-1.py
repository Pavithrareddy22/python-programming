# List of items - each item is represented as a dictionary
items = [
    {"name": "apple", "price": 10, "quantity": 3},
    {"name": "banana", "price": 5, "quantity": 6},
    {"name": "milk", "price": 25, "quantity": 2}
]

# Initialize total cost
total_cost = 0

# Calculate the total cost
for item in items:
    item_total = item["price"] * item["quantity"]
    total_cost += item_total
    print(f"{item['quantity']} x {item['name']} @ {item['price']} = {item_total}")

# Display total bill
print(f"\nTotal Bill: {total_cost}")
