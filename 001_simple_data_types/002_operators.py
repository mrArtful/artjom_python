# ============================================
# Python: Operators (Course Notes)
# ============================================

a = 10
b = 3

# ---- Arithmetic operators ----

# + Addition
print(a + b)          # 13

# - Subtraction
print(a - b)          # 7

# * Multiplication
print(a * b)          # 30

# / Division (always float)
print(a / b)          # 3.3333333333333335
print(type(a / b))    # <class 'float'>

# // Floor division (drops decimals)
print(a // b)         # 3

# % Modulus (remainder)
print(a % b)          # 1

# ** Exponentiation (power)
print(2 ** 3)         # 8


# ---- Comparison operators (result is bool) ----

print(a == b)         # False
print(a != b)         # True
print(a > b)          # True
print(a <= 10)        # True


# ---- Boolean operators ----

is_big = a > 5
is_small = b < 5

print(is_big and is_small)   # True
print(is_big or False)       # True
print(not is_big)            # False


# ---- Common beginner gotchas ----
# 1) / always returns float
print(8 / 2)          # 4.0

# 2) // does NOT round, it just cuts decimals
print(7 // 2)         # 3

# 3) % is useful for even/odd checks
print(10 % 2 == 0)    # True (10 is even)