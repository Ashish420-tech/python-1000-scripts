# check palindrome number
num = int (input(print("Enter a number to check palindrome: ") ))
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if num == rev:
    print(f"{num} is a palindrome number")          
else:
    print(f"{num} is not a palindrome number")