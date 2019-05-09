# Create your Character class logic in here.
# create a Character class to help a Phrase determine how an individual character should display itself

# The Character instance is responsible for holding the state of a given single character. You should ensure when you create
# instances of Character() that you only pass a character that is a single character or len(char) == 1. Anything more or less
# should be invalid and might cause you bugs in your code, especially if you are passing the user's input directly into the
# creation of the Character object.

class Character:
    # create initializer or __init__ that receives a single char paremeter called 'original' or something else
    def __init__(self, original):
    # Have an attribute to store the original
        self.original = original
    # Have an attribute to store a bool of whether or not this letter has had a guess attempted against it
        if self.original == ' ':
            self.was_guessed = True
        else:
            self.was_guessed = False

    def check_guess(self, guess):
    # take a single string char named guess as an arg
    # Update the was_guessed bool to True if guess == original
        self.guess = guess
        if self.guess == self.original:
            self.was_guessed = True
    
    def __str__(self):
        return "{self.original}".format(self=self)

    @property
    def show_guess(self):
    # When called, show original char if was_guessed is True
    # Else show an underscore should be hidden with __
        if self.was_guessed:
            return self.original
        else:
            return "_"
