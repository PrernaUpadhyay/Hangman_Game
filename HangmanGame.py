#Hangman game

import random

# ASCII art for Hangman logo
hangman_logo = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                    __/ |                      
                   |___/                       
'''

# List of words for the game
word_list = ["python", "hangman", "developer", "github", "challenge"]

# ASCII art for the hangman at various stages
hangman_stages = [
    '''
       -----
       |   |
       |   O
       |  /|\\
       |  / \\
       |
    ''',
    '''
       -----
       |   |
       |   O
       |  /|\\
       |  /
       |
    ''',
    '''
       -----
       |   |
       |   O
       |  /|
       |  
       |
    ''',
    '''
       -----
       |   |
       |   O
       |   
       |  
       |
    ''',
    '''
       -----
       |   |
       |   
       |  
       |  
       |
    ''',
    '''
       -----
       |   |
       |   
       |  
       |  
       |
    '''
]


def hangman():
    word = random.choice(word_list)  # Choose a random word
    word_completion = "_" * len(word)  # Create underscores for the word
    guessed = False  # Track if the word has been guessed
    guessed_letters = []  # Store guessed letters
    attempts = 5  # Number of incorrect attempts allowed (0-5)

    print(hangman_logo)  # Display the Hangman logo
    print("Welcome to Hangman!")  # Greet the player
    print(hangman_stages[attempts])  # Show the initial hangman state
    print("Word to guess: ", word_completion)  # Show the word as underscores

    while not guessed and attempts >= 0:  # Change this condition to `>= 0`
        guess = input("Please guess a letter: ").lower()  # Get user input

        if len(guess) == 1 and guess.isalpha():  # Validate input
            if guess in guessed_letters:  # Check for previously guessed letters
                print("You already guessed that letter. Try again.")
            elif guess not in word:  # Check if the letter is not in the word
                print("Incorrect! That letter is not in the word.")
                attempts -= 1  # Reduce attempts
                guessed_letters.append(guess)  # Add to guessed letters
            else:  # Letter is correct
                print("Good job! That letter is in the word.")
                guessed_letters.append(guess)  # Add to guessed letters
                # Update word_completion with the guessed letter
                word_completion = "".join(
                    [guess if letter == guess else word_completion[i] for i, letter in enumerate(word)])

                if "_" not in word_completion:  # Check if the word is completely guessed
                    guessed = True  # Mark as guessed

        else:  # Invalid input
            print("Invalid input. Please enter a single letter.")

        # Show the current state of the game
        print(hangman_stages[attempts])  # Display hangman state
        print("Word to guess: ", word_completion)  # Show current state of the word
        print(f"Guessed letters: {', '.join(guessed_letters)}")  # Show letters guessed
        print(f"Attempts remaining: {attempts}")  # Show remaining attempts

    # End game message
    if guessed:
        print("Congratulations! You've guessed the word:", word)  # Player wins
    else:
        print("Sorry, you've run out of attempts. The word was:", word)  # Player loses


# Run the game
hangman()
