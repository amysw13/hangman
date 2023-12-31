# Hangman 🎲
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Project Aim 📌
To create own implementation of the Hangman game using methods and techniques learned so far on the AI Core journey. 

Including creating classes, defining methods, through encapsulation and abstraction of smaller tasks and finally coding the logic to play the game. 

## Installation and usage instructions ⚙

Download file **milestone_5.py**

To play, run code below in terminal, in the directory where the file was downloaded: 
  
 ```$ python milestone_5.py```


### ReadMe tasks 📋

- [x] A description of the project: what it does, the aim of the project, and what you learned
- [x] Installation instructions
- [x] Usage instructions
- [x] File structure of the project
- [ ] License information


## File structure 🗃

1. [milestone_2.py](milestone_2.py)
   
**Python file for milestone 2:**

  - creating word list
  - randomly choosing word from list using random module and .choice()
  - asking user input for a single letter
  - if statement to validate the input is alphabetic
   
2. [milestone_3.py](milestone_3.py)

**Python file for milestone 3:**

- Creating a while loop for validating input
- While loop defined in function `ask_for_input()`
- Defined function `check_guess` to check if user input letter is present in the randomly chosen word. 
- testing `ask_for_input()`

3. [milestone_4.py](milestone_4.py)

**Python file for milestone 4:**

- Created the Hangman class for the game
- Initiated additional attributes for the game to function
  - list for word_guessed
  - num_letters
  - num_lives
  - list_of_guesses
- Defined in more detail methods of `check_guess()` and `ask_for_input()`
  - validating user input guesses, and if tries before
  - Checking guess letter in randomly selected word and replacing word_guessed list with correctly guessed letter
  - reducing the number of letters left to guess or number of lives if guess is incorrect
- created instance for word_list
- called `ask_for_input()` - to test the method

Additionally, amended the while true loop in milestone_3.py file

4. [milestone_5.py](milestone_5.py)

**Python file for milestone 5:**

- Created function `play_game()` to code in the logic of the game
- Within function creating an instance of the actual game
  - noted that variables needed to have the game instance to ensure they were updated correctly
  - noted that when creating the while true loop, that I needed to code in logical breaks when game was lost or won, so did not run infinitely.
- Final python file to run and play the Hangman game

