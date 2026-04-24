class Entity:

    class_var = 100

    def __init__(self, name, max_hp, class_type):
        self.name = name
        self.max_hp = max_hp
        self.class_type = class_type
        self.current_hp = max_hp

    def take_damage(self, amount):
        self.current_hp -= amount

    def is_alive(self):
        return self.current_hp > 0
    

class Player(Entity):

    def __init__(self, name, max_hp, class_type, xp, level):
        super().__init__(name, max_hp, class_type)
        self.xp = xp
        self.level = level

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= 100:
            self.level += 1
            self.xp = 0


class Enemy(Entity):

    def __init__(self, name, max_hp, class_type, xp_reward, tier):
        super().__init__(name, max_hp, class_type)
        self.xp_reward = xp_reward
        self.tier = tier






ent = Entity("Jack", 200, "warrior")
plr = Player("Bob", 300, "mage", 0, 1)
emy = Enemy("Goblin", 50, "warrior", 30, "common")

# print('lvl', emy.level)

print(ent.class_var)
print(Entity.class_var)
print(plr.class_var)


print(isinstance(ent, Entity))
print(isinstance(plr, Entity))
print(isinstance(plr, Player))
print(isinstance(emy, Player))
print(isinstance(ent, Player))


print(issubclass(Player, Entity))
print(issubclass(Entity, Player))
print(issubclass(Player))

