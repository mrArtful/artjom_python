import json
import os
import random
import questionary

DB_FILE = "data_step3.json"

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def main():
    print("--- Step 3: Persistence (Includes Steps 1-2) ---")
    
    # [From Step 1 & 2] Setup
    history = load_data()
    player_name = questionary.text("What is your name?", default="Player").ask()
    
    choices = ["Rock", "Paper", "Scissors"]
    player_move = questionary.select("Choose move:", choices=choices).ask()
    computer_move = random.choice(choices)
    
    # Logic
    winner = "Draw"
    if player_move != computer_move:
        if (player_move == "Rock" and computer_move == "Scissors") or \
           (player_move == "Paper" and computer_move == "Rock") or \
           (player_move == "Scissors" and computer_move == "Paper"):
            winner = player_name
        else:
            winner = "Computer"
    
    print(f"Winner: {winner}")

    # [New in Step 3] Saving the result
    result = {
        "player": player_name,
        "p_move": player_move,
        "c_move": computer_move,
        "winner": winner
    }
    history.append(result)
    save_data(history)
    print(f"History updated! Total games saved: {len(history)}")

if __name__ == "__main__":
    main()
