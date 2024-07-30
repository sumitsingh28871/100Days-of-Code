#Greetings for the user
print("Welcome to the Tip Calculator")

#Ask the user about the total amount of the bill
bill = float(input("What's your total bill amount?\n"))

#Ask the user how many people user want to split the bill
split = int(input("Between how many people do you want to split the bill?\n"))

#Ask the user about the tip
print("How much tip do you want to give 0%, 2%, 5%, 8%, 10%?/n")
valid_percentage = [0,2,5,8,10]
while True:
    tip_percentage = int(input("Your Choice of tip?\n"))
    if tip_percentage in valid_percentage:
        break
    else:
        print("Please enter the valid tip")

#total amount splitted between the no. of people with tip
total_amount = round(bill + ((tip_percentage/100) * bill), 2)
print(f"The Total amount is {total_amount}")

#amount each person have to contribute
amount_per_person = round(total_amount / split, 2)
print(f"Amount per person is {amount_per_person}")
