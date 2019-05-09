# Create your Phrase class logic here.
# create a Phrase class to handle the creation of phrases

# The Phrase instance might be responsible for things like: Knowing if the entire phrase has been guessed,
# Iterating over its collection of Character to allow a guess to be checked using a Character instance
# method call or to ask the Character object how it should show its letter.

# The instance method names and their implementation are up to you to determine.

import random

import constants
from character import Character

# The class should include an initializer or def __init__ that receives a phrase parameter and holds
# this phrase in an instance attribute on the Phrase object.
class Phrase:
#  A phrase should be a collection of Character objects,
# where each letter of the phrase is a Character() instance stored inside a collection such as a List.
    def __init__(self, phrase):
        self.phrase = [Character(letter) for letter in phrase]
    
    def __iter__(self):
        yield from self.phrase

    def get_phrase(self):
        return random.choice(constants.PHRASES)

    def display_phrase(self):
        for letter in self.phrase:
                print(letter.show_guess, end=' ')
        print()
    
