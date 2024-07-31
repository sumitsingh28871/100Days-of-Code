#Greetings of the program
print("Welcome to the program where you can check whether a year is a Leap Yer or not.")

#Ask the user which year they want to check 
year = int(input("Which year do you want to check?\n"))

#if-elif-else statement to check whether a year is leap or not
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is a Leap Year.".format(year))
        else:
            print("{} is not a Leap Year.".format(year))
    else:
        print("{} is not a Leap Year.".format(year))
else:
    print("{} is not a Leap Year.".format(year))