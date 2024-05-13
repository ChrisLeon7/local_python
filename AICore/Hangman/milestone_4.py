import random

word_list = ["peach", "coconut", "grapefruit", "mango", "grapes"]

word = random.choice(word_list)

class Hangamn:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guesed = ["_"] * len(word)
        self.num_letters = set(word)
        self.num_lives = num_lives
        self.word_list = ["peach", "coconut", "grapefruit", "mango", "grapes"]
        self.list_of_guesses = []

    def check_guess(guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for letter in word:
                if letter == guess:
                    word_guessed = guess
                else:
                    num_lives -= 1
                    print(f'Sorry, {letter} is not in the word')
                    print(f'You have {num_lives} left')
            num_letters -= 1


        else :
                print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input():
        while True:
            guess = input("Enter a letter: ")

            if len(guess) is not 1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in word:
                print("You already tried that letter")
        
        check_guess(guess)
        list_of_guesses.append()

    ask_for_input()

