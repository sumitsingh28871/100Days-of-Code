#Greetings for the Customer
print("Welcome to the Pizza Delivery")

#Ask the customer which size of pizza they want
print("Please select the size of the pizza.\n Small (S): $15\n Medium (M): $20\n Large (L): $25\n")

size = ['S','M','L'] #size of pizza small, medium, large
toppings = ['pepperoni','salami','onion','pineapple','chicken']
while True:
    size_of_pizza = str(input("What size pizza do you want?\n").upper())
    if size_of_pizza in size:
        break
    else:
        print("Please give the correct size of pizza")

#billing
bill = 0

if size_of_pizza == 'S':
    bill += 15
elif size_of_pizza == 'M':
    bill += 20
else:
    bill += 25

#if customer asks for extra cheese
extra_cheese = input("Do you want extra cheese on your pizza? (Y/N)\n").upper()
if extra_cheese == 'Y':
    if size_of_pizza == 'S':
        bill += 2
    else:
        bill += 3
# Inform the customer of the total bill
print(f"The total bill for your {size_of_pizza} size pizza is ${bill}.")