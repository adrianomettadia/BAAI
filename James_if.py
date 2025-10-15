#
# Felicia, 2025/09/24
# File: Felicia_Minus.py
# Short description of the task
#

# 1. Input
products = [
{"name": "Laptop", "price": 1200, "category": "Electronics"},
{"name": "Shirt", "price": 45, "category": "Clothing"},
{"name": "Phone", "price": 800, "category": "Electronics"},
{"name": "Shoes", "price": 120, "category": "Clothing"},
{"name": "Tablet", "price": 350, "category": "Electronics"},
{"name": "Jacket", "price": 95, "category": "Clothing"},
{"name": "Book", "price": 25, "category": "Books"},
{"name": "Headphones", "price": 150, "category": "Electronics"}
]

total_original = 0
total_discount_amount = 0
total_final = 0

print("=== PRODUCTDISCOUNT CALCULATOR ===\n")

for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    # calculate percentage discount
    if category == "Electronics":
        if price >= 1000:
            discount = 0.20
        elif price >=500:
            discount = 0.15
        else :
            discount = 0.10

    elif category == "Clothing":
        if price >= 100:
            discount = 0.25
        else :
            discount = 0.15
    elif category == "Books":
       
            discount = 0.10
    else :
            discount = 0.0 
    
    discount_amount = price *discount
    final_price = price - discount_amount  

    total_original += price
    total_discount_amount += discount_amount 
    total_final += final_price

    print(f"product: {name}")
    print(f"category: {category}")
    print(f"original price: $ {price :.2f}")
    print(f"discount: {discount*100:.0f}%")
    print(f"final price: $ {final_price: 2f}\n")

print("Summary")
print(f"total products: {len(products)}")
print(f"total original price: $ {total_original :.2f}")
print(f"total discount: {total_discount_amount:.2f}")
print(f"total final price: $ {final_price: 2f}")

    


