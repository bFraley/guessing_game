# basic.py - A basic guess a number game implementation.

import os
from random import randint

# Print simple game menu.
def print_menu():
    os.system("clear")
    print("\nGuess a number...\n")
    print("\nGuess a number between 1-100\n")

# Prompt user for number of guesses they would like.
def get_difficulty():
    return(input('\nHow many guesses would you like: '))

# Get a random number between 1 and 100.
def get_random_number():
    return randint(0,100)

# Prompt user for their guess.
def get_guess():
    return input('Your guess: ')

# Run the game loop.
def run_game():

    print_menu()
    max_guesses = get_difficulty()
    target_number = get_random_number()
    guess_count = 0
    run = True

    while run:
        ans = get_guess()

        if not ans.isdigit():
            print('Invalid guess! Please enter a number.')
            break

        if int(ans) == target_number:
            print('CORRECT GUESS, You win!\n')
            run = False
            exit(0)
        else:
            print('Incorrect. Try Again!')
            guess_count += 1


        if guess_count == int(max_guesses):
            print('\nSorry, You Lose\n')
            run = False
            exit(0)

# Start a game.
run_game()
