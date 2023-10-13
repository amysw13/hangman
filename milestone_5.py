import random

class Hangman:

    #class constructor
    def __init__(self, word_list, num_lives=5):
        
        #attributes
        self.word_list = word_list  # Don't hardcode in the list, create a list in the instances of the game
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]  # Create word_guessed with underscores
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    #methods
    #check guess
    def check_guess(self, guess):
        self.guess = guess.lower()

        if self.guess in self.word: 
            print(f"Good guess! {self.guess} is in the word.")
            for letter in self.word: #loop through letters in word
                if letter == guess: #is letter == to guess 
                    guess_index = self.word.index(self.guess) #get index of guess for the word_guess attribute
                    self.word_guessed[guess_index] = self.guess #replace the '_' at the index of the word_guess attribute
            self.num_letters -= 1 #reduce number of letters left to guess
        else:
            self.num_lives-= 1 #reduce the number of lives by one for each try
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")

    #method ask for input
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
        
            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

# Create an instance of the Hangman class
#hangman_game = Hangman(["mangosteen", "mango", "grapes", "oranges", "blueberries"])


# Call the ask_for_input method to test
#hangman_game.ask_for_input()

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives <= 0: #ensure this is the Hangman class instance of num_lives to ensure break out of game
            print("You lost!")
            break 
        elif game.num_letters > 0:
            game.ask_for_input()
        else: 
            print("Congratulations, You won the game!")
            break 

play_game(["mangosteen", "mango", "grapes", "oranges", "blueberries"])

