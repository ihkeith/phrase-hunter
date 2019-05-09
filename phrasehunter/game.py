# Create your Game class logic in here.
# create a Game class with methods for starting the game, handling 
# interactions, getting a random phrase, checking for a win/loss state, and
# removing "lives" or turns from the player

# The class should include an initializer or def __init__ method that receives a phrases parameter and 
# holds these phrases in an instance attribute on the game object.

# You will likely need at least 1 instance attribute:
#     An instance attribute that stores the current Phrase object for the start of the game. You may think of 
#     this as the Active phrase being guessed against by the player while the game is running.

# The Game instance might be responsible for things like: starting the game loop, getting player's 
# input() guesses to pass to a Phrase object to perform its responsibilities against, determining if 
# a win/loss happens after the player runs out of turns or the phrase is completely guessed.
import random

import constants
from character import Character
from phrase import Phrase

class Game:
    def __init__(self, phrase):
        pass

    def get_guess(self, guess):
        pass