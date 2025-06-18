 # factorial using loop
n = int(input(print("Enter a number to find the factorial:")))

fact = 1
for i in range(1,n+1):
    fact *= i
print ("facrorial of {n} is : " , fact)