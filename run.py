# Random number is generated that user attempts to guess.
# The default number of tries is set according to the easy,
# normal, or hard difficulty level. Or, users can specify the
# number of tries on the command line when running the program
# run.py 100.

import sys
from random import randint

class Game(self, max, guesses):

    # Difficulty levels
    diff_levels = {
        'easy': 1,
        'normal': 2,
        'hard':   3
    }

    def print_menu = {
        print('\nGuess the number!!\n')
    }

    def __init__(self):
        self.max = max
        self.guess_count = guess_count
        

    def new_random_number(self):
        return randint(0, self.max)
     
    
