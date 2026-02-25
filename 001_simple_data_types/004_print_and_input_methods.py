# ============================================
# Python: print() and input()
# ============================================

# --------------------------------------------
# print()
# --------------------------------------------
# print() outputs data to the console

print("Hello world")
print(500)
print(3.14)
print(True)

# You can print multiple values
print("Age:", 16)
print("Sum:", 5 + 3)

# print() automatically adds a new line
print("Line 1")
print("Line 2")


# --------------------------------------------
# input()
# --------------------------------------------
# input() reads text from the user
# IMPORTANT: input() ALWAYS returns a string (str)

name = input("Enter your name: ")
print("Hello,", name)
print(type(name))   # <class 'str'>


# --------------------------------------------
# Converting input
# --------------------------------------------
# If you need numbers, you must convert input manually

age = input("Enter your age: ")
age = int(age)

print("Next year you will be", age + 1)


# --------------------------------------------
# Common beginner mistakes
# --------------------------------------------

# ❌ This will NOT work (string + int)
# print("Age:", age + 1)

# ✅ Correct
print("Age:", age)


# --------------------------------------------
# Summary
# --------------------------------------------
# print() → outputs data
# input() → reads user input (always str)
# int(), float() → convert input when needed
