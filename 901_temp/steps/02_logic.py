import questionary
import random

def main():
    print("--- Step 2: Game Logic (Includes Step 1) ---")
    
    # [From Step 1] Basic Interaction
    player_name = questionary.text("What is your name?", default="Player").ask()
    
    # [New in Step 2] Game Mechanics
    choices = ["Rock", "Paper", "Scissors"]
    player_move = questionary.select(
        f"Hi {player_name}, choose your move:",
        choices=choices
    ).ask()
    
    computer_move = random.choice(choices)
    print(f"Computer chose: {computer_move}")
    
    # Win logic
    if player_move == computer_move:
        print("🤝 It's a draw!")
    elif (player_move == "Rock" and computer_move == "Scissors") or \
         (player_move == "Paper" and computer_move == "Rock") or \
         (player_move == "Scissors" and computer_move == "Paper"):
        print(f"🎉 {player_name} wins!")
    else:
        print("💻 Computer wins!")

if __name__ == "__main__":
    main()
