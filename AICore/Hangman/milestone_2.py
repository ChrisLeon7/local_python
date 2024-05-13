import random

word_list = ["peach", "coconut", "grapefruit", "mango", "grapes"]

word = random.choice(word_list)



if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")
