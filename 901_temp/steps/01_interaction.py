import questionary

def main():
    print("--- Step 1: Basic Interaction ---")
    
    # Simple input using questionary
    player_name = questionary.text("What is your name?").ask()
    
    # Simple choice
    move = questionary.select(
        "Choose a move:",
        choices=["Rock", "Paper", "Scissors"]
    ).ask()
    
    print(f"Hello {player_name}, you chose {move}!")

if __name__ == "__main__":
    main()
