# Armstrong Number

# It is a number that is equal to the sum of its own digits, each raised to a power equal to the
# number of digits in the number.

#For example, let's consider the number 153:

#   It has three digits (1, 5, and 3).
#   If we calculate 1^3 + 5^3 + 3^3, we get 1 + 125 + 27, which is equal to 153

# So, 153 is an Armstrong number because it equals the sum of its digits raised to the power
# of the number of digits in the number.

# Another example is 9474

#   It has four digits (9, 4, 7, and 4)
#   If we calculate 9^4 + 4^4 + 7^4 + 4^4, we get 6561 + 256 + 2401 + 256, which is also 
# equal to 9474

# Therefore, 9474 is an Armstrong number as well.

#       Solution:

num = int(input("Enter a number: "))

# Convert the number to a string to easily access each digit and determine the number of digits
num_str = str(num)
num_digits = len(num_str)

# Initialize a variable to store the sum of the digits raised to the power of the number of digits
sum_of_powers = 0
temp_num = num

# Loop through each digit in the number, raise it to the power of the number of digits, and add it to the sum
while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits  # Raise the digit to the power of the number of digits and add it to the sum
    temp_num //= 10                    # Remove the last digit

# After the loop, we compare the sum of the digits raised to the power of the number of digits with the original number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

