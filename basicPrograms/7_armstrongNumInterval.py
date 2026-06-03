# Write a Python Program to Find Armstrong Number in an Interval.

lower = int(input("Enter the lower bound of the interval: "))
upper = int(input("Enter the upper bound of the interval: "))

print(f"Armstrong numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    order = len(str(num))
    temp_num = num
    sum = 0

    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10

    if num == sum:
        print(num)
        





