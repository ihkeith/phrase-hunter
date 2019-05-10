import os
import random
import re

# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
# And just like that, my imports stopped working. The link above helped resolve it
from .phrase import Phrase
from .character import Character

class Game:
    def __init__(self, phrases):
        self.guesses = []
        self.phrases = phrases.copy()
        # self.current_phrase, self.current_hint = Phrase(random.choice(phrases))
        self.current_phrase, self.current_hint = random.choice(phrases)
        self.current_phrase = Phrase(self.current_phrase)
        self.lives = 5

    def get_guess(self):
        guess = ""
        while not guess:
            player_guess = input("Please guess a letter: ")
            if player_guess.isdigit():
                print("That is not a valid guess.")
                continue
            elif len(player_guess) > 1:
                print("That is not a valid guess.")
                continue
            elif not player_guess.isalpha():
                print("That is not a valid guess.")
                continue
            elif player_guess.lower() in self.guesses:
                print("You have already guessed that letter. Please try again")
                continue
            else:
                guess = player_guess
        self.guesses.append(guess.lower())
        if guess.lower() not in [letter.original for letter in self.current_phrase]:
            self.lives -= 1
        return guess.lower()
    
    def game_won(self):
        if self.current_phrase.all_guessed():
            self.clear_screen()
            self.welcome()
            print("Congratulations! You won the game!!")
            print()
            return True
        return False
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def welcome(self):
        welcome = "+++++ Phrase Hunter +++++"
        print("*" * len(welcome))
        print(welcome)
        print("*" * len(welcome))
        print()
        print("Lives Left: {}".format(self.lives))
        print("Letters Guessed: {guesses}\n".format(guesses = self.guesses))
        print("Hint: {}".format(self.current_hint))
        print()
        self.current_phrase.display_phrase()

    def main_loop(self):
        # While game isn't won
        while not self.game_won():
            self.clear_screen()
            self.welcome()
            print()
            # prompt the user for a guess
            player_guess = self.get_guess()
            # check the guess against phrase
            for item in self.current_phrase:
                item.check_guess(player_guess)
            if self.lives == 0:
                self.welcome()
                print("Oh no! You ran out of lives. Please try again later.")
                print()
                break


        