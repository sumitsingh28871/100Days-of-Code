# Greetings for the Customer
print("Welcome to the Pizza Delivery")

# Ask the customer which size of pizza they want
print("Please select the size of the pizza.\n Small (S): $15\n Medium (M): $20\n Large (L): $25\n")
size = ['S', 'M', 'L']  # size of pizza small, medium, large
toppings = ['pepperoni', 'salami', 'onion', 'pineapple', 'chicken']
while True:
    size_of_pizza = str(input("What size pizza do you want?\n").upper())
    if size_of_pizza in size:
        break
    else:
        print("Please give the correct size of pizza")

# Billing
bill = 0

if size_of_pizza == 'S':
    bill += 15
elif size_of_pizza == 'M':
    bill += 20
else:
    bill += 25

# Ask for toppings
choice_of_toppings = str(input("Do you want any toppings on the top? (Y/N)\n").upper())
if choice_of_toppings == 'Y':
    while True:
        selected_topping = input("What topping would you like? (pepperoni, salami, onion, pineapple, chicken)\n").lower()
        if selected_topping in toppings:
            bill += 2  # Assuming each topping adds a fixed amount, e.g., $2
            break
        else:
            print("Please provide a valid topping from the list.")

# If customer asks for extra cheese
extra_cheese = input("Do you want extra cheese on your pizza? (Y/N)\n").upper()
if extra_cheese == 'Y':
    if size_of_pizza == 'S':
        bill += 1
    else:
        bill += 2

# Inform the customer of the total bill
print(f"The total bill for your {size_of_pizza} size pizza is ${bill}.")
