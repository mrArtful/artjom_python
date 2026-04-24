# Homework: The Adventurer's Guild 🗡️
# Build a tiny RPG system using classes and dunder ("magic") methods.
# Part 1 — The Hero class
# Attributes: name (str), hp (int), attack (int), level (int, default 1).
# Implement these dunder methods:

# __init__(self, name, hp, attack, level=1) — initialize a hero.
# __str__ — e.g. "Aragorn (Lv.1) — HP: 100, ATK: 20".
# __repr__ — e.g. "Hero('Aragorn', 100, 20, 1)".
# __eq__ — two heroes are equal if they share the same name and level.
# __lt__ — compare heroes by their power score = hp + attack * 2. This makes sorted([...]) work on a list of heroes.
# __add__ — h1 + h2 returns a new Hero representing a party:

# name: "{a.name} & {b.name}"
# hp and attack: summed
# level: the higher of the two



# Part 2 — The Inventory class
# Stores items (strings) with quantities. Store them internally in a dict, e.g. {"potion": 3, "sword": 1}.

# __init__ — starts empty (or accepts an optional dict).
# A regular method add(item, qty=1).
# __len__ — returns the total quantity of items (not the number of unique items).
# __contains__ — so "potion" in bag works.
# __getitem__ — so bag["potion"] returns the quantity (or 0 if missing — don't raise).
# __str__ — e.g. "Inventory: 3x potion, 1x sword", or "Inventory: empty".