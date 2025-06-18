user_input = input("ชื่อสินค้าและราคา: ")

product_name, price_str = user_input.split()

price = float(price_str)

print(f"Product: {product_name}, Price: {price} THB")