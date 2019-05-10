class Character:
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
        if self.guess.lower() == self.original.lower():
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
