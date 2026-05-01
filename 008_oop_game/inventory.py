class Inventory:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"Picked up: {item["name"]} x {item["qty"]}")

    def show(self):
        if not self.items:
            print('Inventory is empty')
            return
        print("Inventory:")
        for item in self.items:
            print(f'{item['name']} x {item['qty']}')


backpack = Inventory()

backpack.show()

backpack.add({"name": "Health potion", "qty": 6})
backpack.add({"name": "Sword", "qty": 1})
backpack.add({"name": "Mana potion", "qty": 3})

backpack.show()