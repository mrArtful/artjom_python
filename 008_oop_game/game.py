from settings import SEPARATOR
from dice import Dice
from entities import Entity, Warrior, Mage
import time

class Game_Engine:

    def __init__(self):
        self.dice = Dice(6)

    def battle(self, player, enemy):

        while player.is_alive() and enemy.is_alive():
            print(SEPARATOR)
            player.show_status()
            enemy.show_status()
            print(SEPARATOR)
            time.sleep(2)

            self.player_turn(player, enemy)
            if not enemy.is_alive():
                print(f'\n{enemy.name} has been defeated! {player.name} wins!')
                break
            time.sleep(2)

            print(f'--- {enemy.name}s turn ---')
            roll = str(self.dice)
            print(f'Enemy rolls: {roll}')
            enemy.attack(player, roll)

            if not player.is_alive():
                print(f'\n{player.name} has been defeated... Game Over.')
                break

            time.sleep(2)


    def player_turn(self, player, enemy):
        
        while True:
            print(f'\n--- {player.name}s trun ---')
            print('1.Attack')
            print('2.Use Item / Equip Weapon')
            print('3.Special Ability')

            choice = input('Select action: ')

            if choice == '1':
                roll = str(self.dice)
                print(f'You rolled: {roll}')
                player.attack(enemy, roll)
                break
            elif choice == '2':
                pass
            elif choice == '3':
                if isinstance(player, Warrior):
                    player.rage_strike(enemy)
                elif isinstance(player, Mage):
                    player.cast_fireball(enemy)
                else:
                    print('No special abilities available.')
                    continue
                break
            else:
                print('Wrong choice.')
                continue
    

def setup_game():
    print('Welcome to Python RPG')
    while True:
        name = input("Enter your name: ")
        if name:
            break
        else:
            print('Must enter name!')
    
    print("Select class")
    print("1.Warrior (High HP, uses RAGE)")
    print("2.Mage (Magic Power, uses MANA)")
    print("3.Entity (No special powers)")
    while True:
        choice = input('Choice: ')
        if choice == '1':
            player = Warrior(name, 120, 15)
            break
        elif choice == '2':
            player = Mage(name, 80, 10)
            break
        elif choice == '3':
            player = Entity(name, 100, 20)
            break
        else:
            print('Choose wisely!')
            continue
    
    enemy = Entity("Orc", 50, 10)

    return player, enemy


if __name__ == '__main__':

    engine = Game_Engine()
    player, enemy = setup_game()

    engine.battle(player, enemy)