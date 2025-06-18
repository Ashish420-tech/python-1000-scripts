n= int(input(print("Enter a number for check prime:")))

is_prime = all(n%i!=0 for i in range (2,int(n**0.5)+1))
if n>1 and is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")