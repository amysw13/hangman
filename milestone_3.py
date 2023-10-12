import random

word_list = ["mangosteen", "mango", "grapes", "oranges", "blueberries"]
print(word_list)

word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess = guess.lower()

    if guess in word: #isalpha function, checks if str is alphabetic
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
    
        if len(guess) == 1 and guess.isalpha() : #isalpha function, checks if str is alphabetic
           print(f"{guess} is a valid input.")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
        break
    check_guess(guess)

ask_for_input()