# Homework: Inventory Item Classes
#
# Right now, inventory items are stored as plain dictionaries like:
#   {"name": "Health potion", "qty": 6}
#
# Your task is to replace them with proper classes using OOP.
#
# ------------------------------------------------------------------
# TASK 1 - Base Item class
# ------------------------------------------------------------------
# Create a class called Item with:
#   - __init__(self, name, qty=1)  ->  stores name and qty
#   - __str__(self)                ->  returns "Health Potion x 3"
#
# Example:
#   item = Item("Shield", 2)
#   print(item)   # Shield x 2


# ------------------------------------------------------------------
# TASK 2 - Potion subclass
# ------------------------------------------------------------------
# Create a class Potion that inherits from Item with:
#   - __init__(self, name, qty, heal_amount)
#       heal_amount = how many HP it restores
#   - use(self, target)
#       prints: "Artjom drinks Health Potion and restores 50 HP."
#       then restores target.hp by heal_amount (do not exceed target.max_hp)
#       then reduces qty by 1
#       if qty is 0, print: "Health Potion is out of stock."
#
# Example:
#   potion = Potion("Health Potion", 3, 50)
#   potion.use(warrior)


# ------------------------------------------------------------------
# TASK 3 - Weapon subclass
# ------------------------------------------------------------------
# Create a class Weapon that inherits from Item with:
#   - __init__(self, name, qty, bonus_attack)
#       bonus_attack = extra attack damage this weapon adds
#   - equip(self, target)
#       prints: "Artjom equips Sword. Attack increased by 15."
#       then increases target.base_attack by bonus_attack
#
# Example:
#   sword = Weapon("Sword", 1, 15)
#   sword.equip(warrior)