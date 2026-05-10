# Character, Entity - базовый класс для существ
# Warrior, Mage - классы персонажа
# Warrior -> attacks -> +10 Rage | Warrior -> skill -> -30 Rage
# Mage (mana) -> cast spell -> -20 Mana
# Inventory class -> (add, show) -> Warrior -> self.inventory

# base_attack = 10 -> randint(base_attack / 2, base_attack)
# Dice -> d6 (1 - fail -> miss, 6 - critical (x2 base_attack), 2-5 -> base_attack)

from entities import Warrior
from inventory import Weapon

if __name__ == '__main__':
    great_sword = Weapon("Great Sword", 20, 1)
    battle_axe = Weapon("Battle Axe", 25, 1)
    warrior = Warrior("Jack", 120, 20)

    print(f'Name: {warrior.name}, Attack: {warrior.base_attack}, Weapon: {warrior.equiped_weapon}')

    great_sword.equip(warrior)

    print(f'Name: {warrior.name}, Attack: {warrior.base_attack}, Weapon: {warrior.equiped_weapon}')

    battle_axe.equip(warrior)

    print(f'Name: {warrior.name}, Attack: {warrior.base_attack}, Weapon: {warrior.equiped_weapon}')

    great_sword.unequip(warrior)

    print(f'Name: {warrior.name}, Attack: {warrior.base_attack}, Weapon: {warrior.equiped_weapon}')
    

