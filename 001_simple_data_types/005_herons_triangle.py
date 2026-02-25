# ============================================
# Triangle area (Heron's formula)
# ============================================

# Read triangle sides from user
side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))

# Calculate half-perimeter
half_perimeter = (side_a + side_b + side_c) / 2

# Calculate area using Heron's formula
triangle_area = (
    half_perimeter
    * (half_perimeter - side_a)
    * (half_perimeter - side_b)
    * (half_perimeter - side_c)
) ** 0.5

# Output results
print()
print("Triangle sides:")
print("Side A:", side_a)
print("Side B:", side_b)
print("Side C:", side_c)

print()
print("Triangle area:", triangle_area)