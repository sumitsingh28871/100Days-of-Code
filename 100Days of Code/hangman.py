import random

# Greetings for the user
print("Welcome to the Hangman Game")

# List of words
words = ['mouse', 'pokemon', 'camel', 'cat']

# ASCII art stages corresponding to the number of lives left
stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |    
     |    
     |
    -----
    """,
    """
     ------
     |    |
     |    
     |    
     |    
     |
    -----
    """
]

# Number of lives
lives = 6

# Randomly pick a word from the list
chosen_word = random.choice(words)
print(f"Your word has {len(chosen_word)} letters.")  # Give the user a hint about the word length

# Initialize the display with blanks
display = "_ " * len(chosen_word)
print(display)

game_over = False
correct_letters = []

# Main game loop
while not game_over:
    guess = input("Guess a letter: ").lower()

    # Build the display string with the current guessed letters
    new_display = ""
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_ "

    display = new_display
    print(display)

    # If the guessed letter is not in the chosen word
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

    # Always print the current stage of hangman after every guess
    print(stages[lives])

    # Check if the user has won
    if "_" not in display:
        game_over = True
        print("You Win!")

    # Check if the user has lost
    if lives == 0:
        game_over = True
        print("You Lose.")
        print(f"The word was: {chosen_word}")

# End of game
if "_" not in display:
    print("Congratulations! You've guessed the word.")
else:
    print("Game over. Better luck next time!")
