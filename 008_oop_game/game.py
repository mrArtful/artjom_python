from settings import SEPARATOR
from dice import Dice

class Game_Engine:

    def __init__(self):
        self.dice = Dice(6)

    def battle(self, player, enemy):

        print(SEPARATOR)

        while player.is_alive() and enemy.is_alive():
            pass


    def player_turn(self, player, enemy):
        pass