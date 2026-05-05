import random

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def __str__(self):
        return str(random.randint(1, self.sides))
    
