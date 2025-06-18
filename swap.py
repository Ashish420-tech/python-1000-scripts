# Swap three numbers in Python

# Input three numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print(f"Before swapping: a = {a}, b = {b}, c = {c}")

# Swap the numbers (cyclic swap: a->b, b->c, c->a)
a, b, c = c, a, b

print(f"After swapping: a = {a}, b = {b}, c = {c}")25