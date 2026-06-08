# Writing a Python Program to Display Fibonacci Sequence Using Recursion.

# Fibonacci Sequence: 

# The Fibonacci sequence is a series of numbers in which each number is the sum of the two
# preceding ones, usually starting with 0 and 1. In mathematical terms, it is defined by the
# recurrence relation ( F(n) = F(n-1) + F(n-2) ), with initial conditions ( F(0) = 0 ) and ( F(1) = 1
# ). The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. The Fibonacci sequence has
# widespread applications in mathematics, computer science, nature, and art.


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
    
nterms = int(input("Enter the number of terms (greater than 0): "))

if nterms <= 0:
    print("Please enter a positive number: ")
else:
    print("Fibonacci sequence: ")

    for i in range(nterms):
        print(recur_fibo(i))

        


