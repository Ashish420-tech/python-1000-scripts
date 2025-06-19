import math
print("Please enter 2 number to find the GCD   :")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  
gcd = math.gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd}")
# This code calculates the GCD of two numbers using the math library.
# It prompts the user to input two numbers and then uses the gcd function from the math module to compute the GCD.