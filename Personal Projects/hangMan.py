#using random import
import random

import ps

#create a greeting
print("Welcome to Hangman")
#create a word list
words = ["hacker", "random"]


#Ask the user to get a input and choose a letter
secrets_word = random.choice(words)
print(secrets_word)
display_word = []

for letter in secrets_word:
    display_word += "_"
print(display_word)
game_over = False

while not game_over:
    guess = input("Guess a letter").lower()
    for position in range(len(secrets_word)):
        letter = secrets_word[position]
        if letter == guess:
            display_word[position] = letter
    print(display_word)




