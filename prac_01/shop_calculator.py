"""
Shop Calculator
To quickly work out the total price for a number of items, each with different prices.
"""

DISCOUNT_PERCENT = 0.1
total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("The number of items is invalid.")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total -= (total * DISCOUNT_PERCENT)  # Apply discount on total price

print(f"Total price for {number_of_items} items is ${total:.2f}")
