#Heading of the program
print("Welcome to the Even, Odd or Prime Number Program")

#Ask the user to input any number to check whether its a Even, Odd or Prime number
number = int(input("Type any number in your mind?\n"))

#check if it's a even number, odd number, prime number
if number % 2 == 0:
    print("It's an Even Number")
    if number == 2:
        print("It's a Unique Even Prime Number")
else:
    print("It's a Odd Number")
        
    #check for prime number
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            break

    else:
        print("It's a Prime Number")
    