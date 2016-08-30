# basic.py - A basic guess a number game implementation.

import os
from random import randint

# Print simple game menu.
def print_menu():
    os.system("clear")
    print("\nGuess a number...\n")
    print("\nGuess a number between 1-100\n")

# Prompt user for number of guesses they would like.
def get_guess_count():
    guess_count = input('\nHow many guesses would you like: ')

    # Verify guess_count input.
    if not guess_count.isdigit():
        print('Amount of guesses must be a number')  
        return get_guess_count()
    else:
        return int(guess_count)

# Get a random number between 1 and 100.
def get_random_number():
    return randint(0, 100)

# Prompt user for their guess.
def get_guess():
    return input('Your guess: ')

# Run the game loop.
def run_game():
    print_menu()
    max_guesses = get_guess_count()
    target_number = get_random_number()
    guess_count = 0
    run = True
    win = False

    while run:
        # Check guess input.
        guess = get_guess()

        if not guess.isdigit():
            print('Invalid guess! Please enter a number.')
            break

        guess = int(guess)

        # Is the guess correct?
        if guess == target_number:
            win = True
            print('CORRECT GUESS, You win!\n')

        elif guess > target_number:
            print('Too high!')
            guess_count += 1
        
        elif guess < target_number:
            print('Too low!')
            guess_count += 1

        if guess_count == max_guesses and win == False:
            print('\nSorry, You Lose\n')
            run = False
            exit(0)

# Start a game.
run_game()
