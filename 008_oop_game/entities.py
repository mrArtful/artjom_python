class Entity:

    def __init__(self, name, max_hp, base_attack):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.base_attack = base_attack

    def take_damage(self, amount):
        if not amount:
            print('Missed')
        else:
            self.hp = self.hp - amount
            print(f'{self.name} takes {amount} damage! ({self.hp}/{self.max_hp} HP)')
            

    def attack(self, target, dice_result):
        print(f'{self.name} attacks {target.name}')
        if dice_result == '1':
            damage = 0
        elif dice_result == '6':
            damage = 2 * self.base_attack
            print(f'Critical strike, {damage}DMG')
        else:
            damage = self.base_attack
        target.take_damage(damage)

    def is_alive(self):
        return self.hp > 0
    

class Warrior(Entity):

    def __init__(self, name, max_hp, base_attack):
        super().__init__(name, max_hp, base_attack)
        self.rage = 0
        self.max_rage = 100

    def attack(self, target, dice_result):
        print(f'{self.name} attacks {target.name}')
        if dice_result == '1':
            damage = 0
        elif dice_result == '6':
            self.rage += 20
            damage = 2 * self.base_attack
            print(f'Critical strike, {damage}DMG')
        else:
            self.rage += 10
            damage = self.base_attack
        target.take_damage(damage)

    def rage_strike(self, target):
        if self.rage < 30:
            print(f'{self.name} does not have enough rage yet. {self.rage}/{self.max_rage} RAGE')
            return
        self.rage -= 30
        print(f'{self.name} uses a RAGE STRIKE ({self.rage}/{self.max_rage} RAGE left)')
        target.take_damage(self.base_attack * 3)


class Mage(Entity):

    def __init__(self, name, max_hp, base_attack):
        super().__init__(name, max_hp, base_attack)
        self.mana = 70
        self.max_mana = 70

    def cast_fireball(self, target):
        if self.mana < 20:
            print(f'{self.name} does not have enough mana. {self.mana}/{self.max_mana} MANA')
            return
        print(f'{self.name} casts Fireball! {self.mana}/{self.max_mana} MANA')
        self.mana -= 20
        target.take_damage(self.base_attack * 4)
    


warrior = Warrior('Jack', 100, 20)
enemy = Entity('Goblin', 200, 10)
mage = Mage('Merlin', 70, 15)


mage.attack(enemy, '3')
mage.cast_fireball(enemy)
mage.cast_fireball(enemy)
mage.cast_fireball(enemy)
mage.cast_fireball(enemy)