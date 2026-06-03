# Natural numbers are a set of positive integers that are used to count and order objects.
# They are the numbers that typically start from 1 and continue indefinitely, including all the
#whole numbers greater than 0. In mathematical notation, the set of natural numbers is often
# denoted as "N" and can be expressed as:

# N = {1, 2, 3, 4, 5, ...}

# Writing a Python Program to Find the Sum of Natural Numbers.

limit = int(input("Enter the limit: "))
sum = 0

for i in range(1, limit + 1):  
    sum += i 

print(f"The sum of the first {limit} natural numbers is: {sum}")  


