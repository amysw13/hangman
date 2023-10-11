import random

word_list = ["mangosteen", "mango", "grapes", "oranges", "blueberries"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha(): #isalpha function, checks if str is alphabetic
    print("Good guess!")
else: 
    print("Oops! That is not a valid input.")