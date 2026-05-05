from entities import Warrior

class Inventory:

    def __init__(self):
        self.items = []

    def add(self, item):
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.qty += item.qty
                return
        self.items.append(item)

 
    def show_all_items(self):
        if not self.items:
            print('Inventory is empty')
            return
        print("Inventory:")
        for order, item in enumerate(self.items):
            print(f'{order + 1}. {item.name} x {item.qty}')

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
    

    def use_item(self, name, target):
        item = self.get_item_by_name(name)
        if not item:
            print(f'Item {name} was not found!')
            return
        
        if hasattr(item, 'use'):
            item.use(target)
            if item.qty <= 0:
                self.items.remove(item)
        else:
            print(f'{item.name} cannot be used as potion')
        

    

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


if __name__ == "__main__":
    backpack = Inventory()
    potion = Potion("Health Potion", 50, 3)
    big_potion = Potion("Greater Health Potion", 100, 1)
    backpack.show_all_items()

    
    backpack.add(potion)
    backpack.add(big_potion)
    assert len(backpack.items) == 2, "Inventory should stack similar items"
    assert sum([item.qty for item in backpack.items]) == 4, "Items qty is mismatched"

    #################################################
    # qty_list = []
    # for item in backpack.items:
    #     qty_list.append(item.qty)
    # print(qty_list)

    #########################################
    backpack.show_all_items()

    print(backpack.get_item_by_name('health poTion'))
    print(backpack.get_item_by_name('StamIna Pot'))

    warrior = Warrior('Jack', 100, 20)
    warrior.take_damage(30)
    backpack.use_item('health potion', warrior)


# backpack.show()

# backpack.add({"name": "Health potion", "qty": 6})
# backpack.add({"name": "Sword", "qty": 1})
# backpack.add({"name": "Mana potion", "qty": 3})

# backpack.show()