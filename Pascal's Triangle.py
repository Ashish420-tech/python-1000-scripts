def pascal (n):
    for i in range (n):
        val = 1
        for j in range (n-i-1):
            print(" ", end="")
            for k in range (i+1):
                print(val, end=" ")
                val = val * (i -j) // (j + 1)      
        print()

n = 5
pascal(n)