# Mathematically, the Fibonacci sequence can be defined using the following recurrence relation:

# F(0) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛−1)+𝐹(𝑛−2)𝑓𝑜𝑟𝑛 > 1


nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")    
elif nterms == 1:
    print(f"Fibonacci sequence upto {nterms} is: ")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        
        count += 1
