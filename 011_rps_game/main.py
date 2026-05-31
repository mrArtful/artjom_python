import questionary
import random
import os
import json
import datetime
from variables import CHOICES, DB_FILE

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def show_stats(history, player_name):
    if not history:
        print("No history yet.")
        return
    
    mode = questionary.select("Stats View:", choices=["All time", "By Date"]).ask()
    filtered = history

    if mode == "By Date":
        dates = []

        for entry in history:
            dates.append(entry["date_added"][:10])

        dates = list(set(dates))
        dates.sort(reverse=True)
        date_choice = questionary.select("Select Date:", choices=dates).ask()
        filtered = [entry for entry in history if entry["date_added"].startswith(date_choice)]

    total_games = sum(1 for entry in filtered if entry["player"] == player_name)
    wins = sum(1 for entry in filtered if entry["winner"] == player_name)
    print(f"\n--- {mode} Statistics ---")
    print(f"Total games: {total_games}")
    print(f"Your Wins:   {wins}")
    print("-" * 20)
    

def play_round(player_name):

    player_move = questionary.select(
        "Choose a move:",
        choices=CHOICES
    ).ask()

    computer_move = random.choice(CHOICES)

    winner = "Draw"
    if player_move != computer_move:
        if (player_move == CHOICES[0] and computer_move == CHOICES[2]) or \
           (player_move == CHOICES[2] and computer_move == CHOICES[1]) or \
           (player_move == CHOICES[1] and computer_move == CHOICES[0]):
            winner =  player_name
        else:
            winner = "Computer"
    print(f"Computer chose {computer_move}. Result: {winner}")

    return {
        "date_added": str(datetime.datetime.now()),
        "player": player_name,
        "winner": winner,
    }

def main():
    print("Welcome to Rock Paper Scissors game!")
    history = load_data()
    player_name = questionary.text("What is your name?").ask()
    
    while True:
        action = questionary.select(
            "Main menu:",
            choices=["Play round", "View stats", "Clear history", "Exit"]
        ).ask()

        if action == "Exit":
            break
        elif action == "Play round":
            result = play_round(player_name)
            if result:
                history.append(result)
                save_data(history)
        elif action == "View stats":
            show_stats(history, player_name)
        elif action == "Clear history":
            if questionary.confirm("Delete everything?").ask():
                history = []
                save_data(history)

if __name__ == '__main__':
    main()