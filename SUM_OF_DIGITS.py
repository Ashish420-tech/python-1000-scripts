num = int (input(print("Enter a number to find the sum of digits:")))

total = sum (int(d)for d in str(num))
print(f"The sum of the digits of {num} is {total}.")
# Output: The sum of the digits of 12345 is 15.
# This code takes a number as input and calculates the sum of its digits.