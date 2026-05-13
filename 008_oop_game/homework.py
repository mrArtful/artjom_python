"""
RPG GAME - INVENTORY HOMEWORK

Welcome to the Inventory expansion homework! 
Your goal is to integrate the Inventory system into the existing RPG game.

--- TASK 1 (Beginner) ---
In 'entities.py', modify the Entity class to include an inventory.
Every character should start with an empty Inventory instance (from inventory.py).

--- TASK 2 (Intermediate) ---
In 'inventory.py', create a new class 'ManaPotion' that inherits from 'Potion'.
Instead of healing HP, it should restore MANA for Mages.
Hint: Check if the target has the 'mana' attribute before trying to restore it.

--- TASK 3 (Advanced) BONUS ---
In 'game.py', implement the 'Item Menu' logic.
When the player chooses '2. Use Item / Equip Weapon':
1. Show all items in the inventory.
2. Ask the player to enter the name of the item they want to use/equip.
3. Use the item on the player.
"""