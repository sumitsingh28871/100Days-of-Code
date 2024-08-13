#Password Generator Project
import random

#Greetings
print("Welcome to the Password Generator Program")


def pass_gen(length):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = [random.choice(letters), random.choice(numbers), random.choice(symbols), random.choice(upper_letters)]
    
    # Combine all characters
    all_characters = letters + upper_letters + numbers + symbols

    password += random.choices(all_characters, k=length - len(password))

    # Shuffle to avoid predictable sequences
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

# Ask the user for the desired password length
length = int(input("Enter the desired password length: "))

# Generate and display the password
generated_password = pass_gen(length)
print(f"Your generated password is: {generated_password}")
    