from phrasehunter import constants
from phrasehunter.game import Game

if __name__ == '__main__':
    game = Game(constants.PHRASES)
    game.main_loop()