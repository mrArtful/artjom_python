from entities import Warrior
class Item:

    def __init__(self, name, qty=1):
        self.name = name
        self.qty = qty

    def __str__(self):
        return f"{self.name} x {self.qty}"
    

class Potion(Item):

    def __init__(self, name, heal_amount, qty=1):
        super().__init__(name, qty)
        self.heal_amount = heal_amount

    def use(self, target):
        if self.qty > 0:
            if target.hp < target.max_hp:
                print(f'{target.name} drinks {self.name} and restores {self.heal_amount} HP.')
                self.qty -= 1
                if target.hp + self.heal_amount > target.max_hp:
                    target.hp = target.max_hp
                else:
                    target.hp += self.heal_amount
            else:
                print(f'{target.name} has full HP.')
        else:
            print(f"{self.name} is out of stock.")
        

class Weapon(Item):

    def __init__(self, name, bonus_attack, qty=1):
        super().__init__(name, qty)
        self.bonus_attack = bonus_attack

    # TODO Пересмотреть метод надевания предмета
    # 
    def equip(self, target):
        print(f'{target.name} equips {self.name}. Attack increased by {self.bonus_attack}')
        target.base_attack += self.bonus_attack


if __name__ == '__main__':
    warrior = Warrior("Jack", 100, 30)
    potion = Potion("Health Potion", 50, 3)

    assert warrior.hp == warrior.max_hp, "Warrior HP is not equal to max_hp"
    warrior.take_damage(20)
    assert warrior.hp == warrior.max_hp - 20, "Difference in HP after damage"
    potion.use(warrior)
    assert warrior.hp == warrior.max_hp, f"HP over max HP limit ({warrior.hp} / {warrior.max_hp} HP)"
    assert potion.qty == 2, f"Wrong potion qty"
