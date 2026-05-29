# Prime Numbers:

# A prime number is a whole number that cannot be evenly divided by any other number
# except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
# cannot be divided by any other positive integer except for 1 and their own value.

# num = int(input("Enter a number: "))

# # define a flag variable
# flag = False
# if num == 1:
#     print(f"{num} is not a prime number ")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True     # If factor is found, set flag to True
#             break          # breakx out of the loop

# if flag:                    # checkx if flag is True
#     print(f"{num} is not a prime number")
# else:
#     print(f"{num} is a prime number")


# Program to display all the prime numbers within an interval

lower = 1
upper = int(input("Enter the upper limit number:  "))

print(f"Prime numbers between {lower} and {upper} are: ")

for num in range(lower, upper + 1):
    # All prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


