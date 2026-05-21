import questionary

"""
HOMEWORK: Introduction to Questionary
Topic: RPG Game Interface

Your task is to replace the standard input() and print() based logic with 
the questionary library to create a more interactive CLI experience.
"""

# -----------------------------------------------------------------------------
# TASK 1: Character Naming
# Use questionary.text() to ask the user for their hero's name.
# Requirement: The name cannot be empty.
# -----------------------------------------------------------------------------

def get_character_name():
    # TODO: Replace with questionary.text(...)
    name = input("Enter your hero's name: ")
    return name


# -----------------------------------------------------------------------------
# TASK 2: Class Selection
# Use questionary.select() to choose a character class.
# Choices: "Warrior", "Mage", "Rogue", "Paladin"
# -----------------------------------------------------------------------------

def choose_class():
    # TODO: Replace with questionary.select(...)
    print("Select your class:")
    print("1. Warrior\n2. Mage\n3. Rogue\n4. Paladin")
    choice = input("Choice: ")
    return choice


# -----------------------------------------------------------------------------
# TASK 3: Difficulty Confirmation
# Use questionary.confirm() to ask: "Are you ready to enter the Hardcore mode?"
# Default should be False.
# -----------------------------------------------------------------------------

def confirm_hardcore():
    # TODO: Replace with questionary.confirm(...)
    choice = input("Enter Hardcore mode? (y/n): ")
    return choice.lower() == 'y'


# -----------------------------------------------------------------------------
# TASK 4: Action Menu
# Use questionary.select() to show available actions in a room.
# Choices: "Search the room", "Open the chest", "Talk to NPC", "Leave room"
# -----------------------------------------------------------------------------

def room_actions():
    # TODO: Replace with questionary.select(...)
    print("What do you want to do?")
    choice = input("Action: ")
    return choice


if __name__ == "__main__":
    print("--- RPG Character Setup ---")
    name = get_character_name()
    char_class = choose_class()
    is_hardcore = confirm_hardcore()
    
    print(f"\nHero: {name}, Class: {char_class}, Hardcore: {is_hardcore}")
    
    action = room_actions()
    print(f"Executing: {action}")
