"""
HOMEWORK: The Equipment Slot

CONTEXT:
Currently, when a character equips a weapon, their `base_attack` is increased directly.
However, we have no way of knowing WHICH weapon is equipped, and if we equip a second 
weapon, the bonuses just keep stacking infinitely!

TASK:
1. Modify the `Entity` class (in entities.py) or extend it here to have an `equipped_weapon` attribute.
2. Update the `Weapon` class below:
    - Implement `equip(self, target)`: 
        - It should check if the target already has a weapon.
        - If yes, it should unequip the old weapon first (subtract its bonus).
        - Then, it should add the new weapon's bonus and set `target.equipped_weapon = self`.
    - Implement `unequip(self, target)`:
        - It should subtract the bonus and set `target.equipped_weapon = None`.

GOAL: 
Ensure that a character can only have ONE weapon equipped at a time, and switching 
weapons correctly calculates the final attack power.
"""
