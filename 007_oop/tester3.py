class Entity:

    class_var = 100

    def __init__(self, name, max_hp, class_type):
        self.name = name
        self.max_hp = max_hp
        self.class_type = class_type
        self.__current_hp = max_hp

    @property
    def hp(self):
        return self.__current_hp
    
    @hp.setter
    def hp(self, amount):
        self.__current_hp = amount

    @hp.deleter
    def hp(self):
        del self.__current_hp

    def take_damage(self, amount):
        self.current_hp -= amount

    def __bool__(self):
        return self.current_hp > 0
    
    def __str__(self):
        return f'{self.name} HP: {self.max_hp} CLASS: {self.class_type}'
    
    def __repr__(self):
        return f'Entity("{self.name}", "{self.max_hp}", "{self.class_type}")'
    
    def __add__(self, other):
        return self.current_hp + other.current_hp
    
    def __len__(self):
        return len(self.name)
    



slime = Entity("Blue slime", 0, "monster")
warrior = Entity("Arthur", 200, "warrior")

print(warrior._Entity__current_hp)
print(warrior.__dict__)

print(warrior.hp)
warrior.hp = 10000
print(warrior.hp)
del warrior.hp
print(warrior.__dict__)

# print(slime + warrior)

# print(len(slime))

# # print(slime)
# # print(repr(slime))

# print(bool(slime))

# print(str.__add__('hello', 'world'))