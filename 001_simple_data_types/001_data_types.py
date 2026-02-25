# ============================================
# Python: Variables + Simple Data Types
# int, float, str, bool, None
# ============================================

# --------------------------------------------
# Comments
# --------------------------------------------
# If you want to comment out a line in Python, put "#" at the beginning.
# print(500)  # This line will NOT run

# --------------------------------------------
# Printing to the console
# --------------------------------------------
# print() is used to output something to the console.
print("Hello, Python!")   # string example
print(500)                # int example

# --------------------------------------------
# type() — check a value's data type
# --------------------------------------------
# type() returns the data type (class) of the value you pass in.
print(type(500))          # <class 'int'>
print(type(50.0))         # <class 'float'>
print(type("Hello"))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type(None))         # <class 'NoneType'>

# --------------------------------------------
# help() — get help about something
# --------------------------------------------
# help() shows documentation.
# NOTE: help(500) is not very useful for beginners.
# It's more useful to ask help about a function or a type:
# help(print)
# help(int)

# --------------------------------------------
# Variables
# --------------------------------------------
# variable_name = variable_value
# A variable is just a "label" pointing to a value.

a = 500
print("a =", a)
print("type(a) =", type(a))

# Reassigning: same variable name, new value
a = 501
print("a reassigned =", a)