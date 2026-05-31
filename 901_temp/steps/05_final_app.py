import json
import os
import random
import datetime
import questionary

# FINAL APP - The complete, refined version of everything learned
HISTORY_FILE = 'game_history_final.json'

def load_history():
    if not os.path.exists(HISTORY_FILE): return []
    try:
        with open(HISTORY_FILE, 'r') as f: return json.load(f)
    except: return []

def save_history(h):
    with open(HISTORY_FILE, 'w') as f: json.dump(h, f, indent=4)

def show_stats(history, name):
    """[New in Step 5] Advanced Data Analysis"""
    if not history: 
        print("No history yet.")
        return
    
    mode = questionary.select("Stats View:", choices=["All time", "By Date"]).ask()
    filtered = history
    
    if mode == "By Date":
        dates = sorted(list(set(e['timestamp'][:10] for e in history)), reverse=True)
        d = questionary.select("Select Date:", choices=dates).ask()
        filtered = [e for e in history if e['timestamp'].startswith(d)]
    
    wins = sum(1 for e in filtered if e.get('winner') == name)
    print(f"\n--- {mode} Statistics ---")
    print(f"Total Games: {len(filtered)}")
    print(f"Your Wins:   {wins}")
    print("-" * 20)

def play_round(name):
    choices = ["Rock", "Paper", "Scissors"]
    p_move = questionary.select("Your Move:", choices=choices).ask()
    if not p_move: return None
    
    c_move = random.choice(choices)
    if p_move == c_move: winner = "Draw"
    elif (p_move == "Rock" and c_move == "Scissors") or \
         (p_move == "Paper" and c_move == "Rock") or \
         (p_move == "Scissors" and c_move == "Paper"):
        winner = name
    else: winner = "Computer"
    
    print(f"\nComputer: {c_move} | Winner: {winner}")
    return {"timestamp": str(datetime.datetime.now()), "winner": winner}

def main():
    print("Welcome to the Ultimate Rock Paper Scissors!")
    history = load_history()
    name = questionary.text("What is your name?", default="Player").ask()
    
    while True:
        # [New in Step 5] Main Menu interface
        action = questionary.select(
            "Main Menu:",
            choices=["Play Round", "View Stats", "Clear History", "Exit"]
        ).ask()

        if action == "Exit":
            break
        elif action == "Play Round":
            res = play_round(name)
            if res:
                history.append(res)
                save_history(history)
        elif action == "View Stats":
            show_stats(history, name)
        elif action == "Clear History":
            if questionary.confirm("Delete everything?").ask():
                history = []
                save_history(history)

if __name__ == "__main__":
    main()
