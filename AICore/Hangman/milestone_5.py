import random

class Hangamn:
    
    def __init__(self, word_list, num_lives):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = set(self.word)
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters.remove(guess)
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} left')
            

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
        


def play_game():
    word_list = ["peach", "coconut", "grapefruit", "mango", "grapes"]
    num_lives = 5
    game = Hangamn(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You have lost")
            break
        elif len(game.num_letters) > 0:
            game.ask_for_input()
        elif num_lives != 0 and len(game.num_letters) <= 0:
            print("Congratulations. You won the game.")
            break


play_game()

