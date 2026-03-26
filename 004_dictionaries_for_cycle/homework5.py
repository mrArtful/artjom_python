# Task 1
# if / elif / else
# Grade calculator

# Write a function get_grade(score) that accepts a number from 0 to 100 and returns the letter grade.

# 90–100 → "A"
# 75–89 → "B"
# 60–74 → "C"
# below 60 → "F"
# if the score is outside 0–100, return "Invalid score"
# print(get_grade(92)) # → "A"
# print(get_grade(55)) # → "F"
# print(get_grade(110)) # → "Invalid score"




# Task 2
# for / else
# Find the first even number

# Write a function find_first_even(numbers) that receives a list of integers and returns the first even number it finds. If there are no even numbers in the list, return the string "Not found".

# Use a for loop with an else clause
# Stop the loop as soon as the first even number is found
# Do not use any built-in like filter()
# print(find_first_even([3, 7, 4, 9])) # → 4
# print(find_first_even([1, 3, 5, 7])) # → "Not found"



# Task 3
# while
# Guess the number game

# Write a program that picks a secret number (you can hardcode it) and asks the user to guess it in a loop. Give hints after each wrong guess.

# Use a while loop that runs until the user guesses correctly
# Print "Too high!" or "Too low!" after each wrong guess
# Count the number of attempts and print it when the user wins
# If the user types quit, end the game early
# Guess a number (1–100): 50
# Too high!
# Guess a number (1–100): 25
# Too low!
# Guess a number (1–100): 37
# Correct! You got it in 3 tries.



# Task 4
# try / except / else
# Safe division calculator

# Write a function safe_divide(a, b) that divides two numbers safely, handling all possible input errors.

# Catch ZeroDivisionError and return "Cannot divide by zero"
# Catch TypeError (e.g. letters passed in) and return "Invalid input: numbers only"
# Use the else clause to print "Division successful" only when no error occurred
# Use finally to always print "Operation complete"
# safe_divide(10, 2) # → 5.0
# safe_divide(10, 0) # → "Cannot divide by zero"
# safe_divide("a", 2) # → "Invalid input: numbers only"