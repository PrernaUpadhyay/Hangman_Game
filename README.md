

---

# Hangman Game 🎮

This Python project is a simple command-line version of the **Hangman** game. The game randomly selects a word from a list, and the player must guess the word one letter at a time. With each incorrect guess, a part of the hangman is drawn. The player wins by guessing the word before the hangman is fully drawn.

## How to Play

1. Start the Game:  
   The program selects a random word from the word list.
   
2. Input:  
   You are prompted to guess a letter. The game shows the current state of the word, with unguessed letters represented by underscores (`_`).

3. Guesses:  
   - Correct guesses reveal the letter in the word.
   - Incorrect guesses draw part of the hangman and decrease your remaining attempts.

4. Win Condition:  
   Guess the word before running out of attempts. If you successfully guess all the letters, you win!

5. Lose Condition:  
   If the hangman is fully drawn (i.e., you run out of attempts), you lose, and the correct word is revealed.

## Example Gameplay

```bash
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

Welcome to Hangman!
Word to guess:  _____
Please guess a letter: a
Good job! That letter is in the word.
Word to guess:  _a__a_
Attempts remaining: 5
```

## Features

- ASCII Art: Fun, visual ASCII art for the hangman.
- Random Word Selection: The game randomly selects a word from a predefined list.
- Input Validation: Ensures that the user input is valid (single letters only).
- Tracking Guesses: Keeps track of previously guessed letters.
- Game Feedback: Provides feedback on correct and incorrect guesses, and shows the hangman state with each incorrect attempt.


Let me know if you'd like any changes or if you'd like to add additional sections!
