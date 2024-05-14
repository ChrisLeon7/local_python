import random

word_list = ["peach", "coconut", "grapefruit", "mango", "grapes"]

word = random.choice(word_list)

class Hangamn:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guesed = ["_"] * len(word)
        self.num_letters = set(self.word)
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed = guess
            self.num_letters.remove(guess)
        else:
            num_lives -= 1
            print(f'Sorry, {letter} is not in the word')
            print(f'You have {num_lives} left')
            

    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")
            if len(guess) == 1 and guess.isalpha() and guess not in self.list_of_guesses:
                self.list_of_guesses.append(guess)
                break
            elif guess in self.list_of_guesses:
                print("You already tried that letter.")
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        self.check_guess(guess)
        self.list_of_guesses.append()


def play_game(word_list):
    num_lives = 5
    game = Hangamn(word_list)
    game(word_list, num_lives)
    while True:
        if num_lives == 0:
            print("You have lost")
        elif game.num_letters > 0:
            game.ask_for_input()
        elif num_lives != 0 and game.num_letters <= 0:
            print("Congratulations. You won the game.")

play_game(word_list)

