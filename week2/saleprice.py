product_description = input("Please enter the product description: ")
product_quantity = int(input(f"How many of {product_description} are being purchased?: "))
regular_price = float(input("What is the regular price?: "))

state_tax = 0.065

if regular_price <= 19.99:
    total_price = float(regular_price * product_quantity)
    tax = (total_price * state_tax)
    price_after_tax = (total_price * state_tax) + total_price
    savings = 0
elif regular_price > 19.99 and regular_price <= 39.99:
    print("You have a 15 percent discount!")
    discount = regular_price * 0.15
    price_after_discount = regular_price - discount
    total_price = float(price_after_discount * product_quantity)
    tax = (total_price * state_tax)
    price_after_tax = (total_price * state_tax) + total_price
    savings = discount * product_quantity
elif regular_price > 39.99:
    print("You have a 25 percent discount!")
    discount = regular_price * 0.25
    price_after_discount = regular_price - discount
    total_price = float(price_after_discount * product_quantity)
    tax = (total_price * state_tax)
    price_after_tax = (total_price * state_tax) + total_price
    savings = discount * product_quantity
print("\n")
print("Your Receipt")
print("--------------------------------------------------")
print(f"{product_quantity} {product_description}(s) @ ${price_after_discount} each.")
print(f"Sales tax: ${tax}")
print(f"Total amount due: ${price_after_tax:.2f}")
print(f"You saved ${savings:.2f} today.") 