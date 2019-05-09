# Create your Game class logic in here.
# create a Game class with methods for starting the game, handling 
# interactions, getting a random phrase, checking for a win/loss state, and
# removing "lives" or turns from the player

# You will likely need at least 1 instance attribute:
#  An instance attribute that stores the current Phrase object for the start of the game. You may think of 
#  this as the Active phrase being guessed against by the player while the game is running.

# The Game instance might be responsible for things like: starting the game loop, getting player's 
# input() guesses to pass to a Phrase object to perform its responsibilities against, determining if 
# a win/loss happens after the player runs out of turns or the phrase is completely guessed.
import os
import random

from .phrase import Phrase
from .character import Character

class Game:
    def __init__(self, phrases):
        self.guesses = []
        self.phrases = phrases.copy()
        self.current_phrase = Phrase(random.choice(phrases))
        self.lives = 5

    def get_guess(self):
        # Prompt player for guess
        # Check if valid guess (not num and not more than one char)
        # Update guesses list
        # Return guess
        guess = ""
        while not guess:
            player_guess = input("Please guess a letter: ")
            if player_guess.isdigit():
                print("That is not a valid guess.")
                continue
            elif len(player_guess) > 1:
                print("That is not a valid guess.")
                continue
            else:
                guess = player_guess
        self.guesses.append(guess)
        return guess.lower()
    
    # def lives(self):
    #     pass
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def welcome(self):
        welcome = "Welcome to Phrase Hunter"
        print("*" * len(welcome))
        print(welcome)
        print("*" * len(welcome))
        print("Lives Left: {}".format(self.lives))
        print("Letters Guessed: {guesses}\n".format(guesses = self.guesses))
        self.current_phrase.display_phrase()

    def main_loop(self):
        self.clear_screen()
        self.welcome()
        # While game isn't won
        # prompt the user for a guess
        # check the guess against phrase
        self.get_guess()
        print(self.guesses)

        