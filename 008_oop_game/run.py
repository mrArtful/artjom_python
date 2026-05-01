# Character, Entity - базовый класс для существ
# Warrior, Mage - классы персонажа
# Warrior -> attacks -> +10 Rage | Warrior -> skill -> -30 Rage
# Mage (mana) -> cast spell -> -20 Mana
# Inventory class -> (add, show) -> Warrior -> self.inventory

# base_attack = 10 -> randint(base_attack / 2, base_attack)
# Dice -> d6 (1 - fail -> miss, 6 - critical (x2 base_attack), 2-5 -> base_attack)

from dice import Dice

d6 = Dice(6)



if __name__ == '__main__':
    print(d6)