# discount.py
import datetime

# Get the subtotal from the user
subtotal = 0
while True:
    price = input("Enter the price of the item (or 0 to finish): ")
    price = float(price)  # Corrected here
    if price == 0:
        break  # Exit the loop if the price is 0
    quantity = input("Enter the quantity: ")
    quantity = float(quantity)  # Corrected here
    subtotal += price * quantity

# Get the day of the week from your computer's operating system
day_of_week = datetime.datetime.today().weekday() # Monday is 0 and Sunday is 6

# # Test purpose
# day_of_week = 1

# Initialize discount variable
discount = 0

# If the subtotal is $50 or greater and today is Tuesday (1) or Wednesday (2)
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    # Subtract 10% from the subtotal
    discount = subtotal * 0.1
    subtotal -= discount
    print(f"\nDiscount amount: ${discount:.2f}")

elif(day_of_week == 1 or day_of_week == 2 ) and (subtotal < 50):
    difference = 50 - subtotal
    print(f"\nYou need to purchase and additional item of ${difference:.2f} or more to receive the discount.")  # Corrected here

# Compute the total amount due by adding sales tax of 6% to the subtotal
sales_tax = subtotal * 0.06
total_amount_due = subtotal + sales_tax

# Print the sales tax amount and the total amount due
print(f"Sales tax amount: ${sales_tax:.2f}")
print(f"Total amount due: ${total_amount_due:.2f}")