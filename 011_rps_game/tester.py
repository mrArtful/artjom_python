import questionary
import random
from variables import CHOICES


result = []
def play_round():

    player_move = random.choice(CHOICES)
    computer_move = random.choice(CHOICES)

    winner = "Draw"
    if player_move != computer_move:
        if (player_move == CHOICES[0] and computer_move == CHOICES[2]) or \
           (player_move == CHOICES[2] and computer_move == CHOICES[1]) or \
           (player_move == CHOICES[1] and computer_move == CHOICES[0]):
            winner =  player_move
        else:
            winner = computer_move
    result.append(winner)

x = 0
while x < 10:
    play_round()
    x += 1

print(CHOICES[0], result.count(CHOICES[0]))
print(CHOICES[1], result.count(CHOICES[1]))
print(CHOICES[2], result.count(CHOICES[2]))