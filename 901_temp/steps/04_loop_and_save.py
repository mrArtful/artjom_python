import json
import os
import random
import datetime
import questionary

HISTORY_FILE = 'game_history_step4.json'

def load_history():
    if not os.path.exists(HISTORY_FILE): return []
    try:
        with open(HISTORY_FILE, 'r') as f: return json.load(f)
    except: return []

def save_history(h):
    with open(HISTORY_FILE, 'w') as f: json.dump(h, f, indent=4)

def play_round(player_name):
    # [From Step 2 logic]
    choices = ["Rock", "Paper", "Scissors"]
    player_move = questionary.select("Move:", choices=choices).ask()
    if not player_move: return None
    
    computer_move = random.choice(choices)
    winner = "Draw"
    if player_move != computer_move:
        if (player_move == "Rock" and computer_move == "Scissors") or \
           (player_move == "Paper" and computer_move == "Rock") or \
           (player_move == "Scissors" and computer_move == "Paper"):
            winner = player_name
        else:
            winner = "Computer"
    
    print(f"Computer chose {computer_move}. Result: {winner}")
    
    return {
        "timestamp": str(datetime.datetime.now()),
        "player": player_name,
        "winner": winner
    }

def main():
    print("--- Step 4: Game Loop (Includes Steps 1-3) ---")
    history = load_history()
    name = questionary.text("Player Name:").ask()
    
    # [New in Step 4] Replayability using a Loop
    while True:
        result = play_round(name)
        if result:
            history.append(result)
            save_history(history)
        
        if not questionary.confirm("Play again?").ask():
            break
            
    print(f"Thanks for playing, {name}! You played {len(history)} games in total.")

if __name__ == "__main__":
    main()
