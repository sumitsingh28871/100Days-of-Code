#Greetings
print("Welcome to the Love Calculator, Let's find out your compatability.")

#ask the name of the user and whom they want to check their compatability
FirstPerson = str(input("What is your name?\n")).upper()
SecondPerson = str(input("What is the name of the person whom do you want to check the compatability with?\n")).upper()

#combine both names
CombinedName = FirstPerson + SecondPerson

#count TRUE & LOVE in combined name
T = CombinedName.count('T')
R = CombinedName.count('R')
U = CombinedName.count('U')
E = CombinedName.count('E')
FirstDigit = T + R + U + E

L = CombinedName.count('L')
O = CombinedName.count('O')
V = CombinedName.count('V')
E = CombinedName.count('E')
SecondDigit = L + O + V + E

#Calculating the Score
FinalScore = str(FirstDigit) + str(SecondDigit)

#messages on the basis of score
if int(FinalScore) < 10 or int(FinalScore) > 90:
    print(f"Your Score is {FinalScore}, You go together like Coke & Mentos")

elif 40 <= int(FinalScore) <= 60:
    print(f"Your Score is {FinalScore}, You are alright together.")

else:
    print(f"Your Score is {FinalScore}.")
