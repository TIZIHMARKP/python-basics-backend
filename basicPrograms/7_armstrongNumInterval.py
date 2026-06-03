# Write a Python Program to Find Armstrong Number in an Interval.

lower = int(input("Enter the lower bound of the interval: "))
upper = int(input("Enter the upper bound of the interval: "))

print(f"Armstrong numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):  # Loop through the numbers in the specified interval
    order = len(str(num))     # Calculate the number of digits in the current number (order)
    temp_num = num
    sum = 0

    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
        
    # After the loop, we check if the calculated sum is equal to the original number
    if num == sum:
        print(num)






