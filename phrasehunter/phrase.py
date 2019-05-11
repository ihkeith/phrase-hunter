from .character import Character

class Phrase:
    def __init__(self, phrase):
        # self.phrase, self.hint = phrase
        # self.phrase = [Character(letter) for letter in self.phrase]
        self.phrase = [Character(letter) for letter in phrase[0]]
        self.hint = phrase[1]
    
    def __iter__(self):
        yield from self.phrase

    def all_guessed(self):
        guessed = []
        for self.letter in self.phrase:
            if self.letter.was_guessed:
                guessed.append(self.letter)
        if len(guessed) == len(self.phrase):
            return True

    def display_phrase(self):
        for letter in self.phrase:
                print(letter.show_guess, end=' ')
        print()
    
