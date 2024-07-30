#Greetings for the user
print("Welcome to the Life in Weeks Program")

#Ask the user about their age
age = int(input("What's your Age?\n"))

#Setting up the imaginary maximum age
Live_until = 90

#Getting the remaining years by subtracting the user age from maximum age
remaining_years = Live_until - age

#converting years into weeks
remaining_weeks = round(remaining_years * 52.1775, 2)
print(f"You have {remaining_weeks} weeks left to live") 
