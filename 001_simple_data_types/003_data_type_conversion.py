# ============================================
# Python: Data Type Conversion
# int, float, str, bool, None
# ============================================

# --------------------------------------------
# Original values
# --------------------------------------------
int_var = 500
float_var = 50.9
str_num = "123.2"
str_text = "Hello world"
none_var = None

print(int_var, type(int_var))
print(float_var, type(float_var))
print(str_num, type(str_num))
print(str_text, type(str_text))
print(none_var, type(none_var))


# --------------------------------------------
# int <-> float
# --------------------------------------------

# int → float
result = float(int_var)
print(result, type(result))     # 500.0

# float → int (decimal part is removed, NOT rounded)
result = int(float_var)
print(result, type(result))     # 50


# --------------------------------------------
# str → number
# --------------------------------------------

# str → float (must look like a number)
result = float(str_num)
print(result, type(result))     # 123.2

# float → int
result = int(result)
print(result, type(result))     # 123

# ❌ Impossible conversion (will raise an error)
# int("Hello world")


# --------------------------------------------
# Conversion to bool (Truthy / Falsy)
# --------------------------------------------

# ---- Numbers ----
print(bool(0))        # False
print(bool(1))        # True
print(bool(-5))       # True

print(bool(0.0))      # False
print(bool(0.1))      # True

# ---- Strings ----
print(bool(""))       # False (empty string)
print(bool(" "))      # True  (space is still a character)
print(bool("False"))  # True  (text content does not matter)

# ---- None ----
print(bool(None))     # False


# --------------------------------------------
# Summary: False values in Python
# --------------------------------------------
# These values are considered False:
# 0
# 0.0
# ""
# None
# False

# Everything else is True