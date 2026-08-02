# A Disarium number is a number that is equal to the sum of its digits each raised to 
# the power of its respective positions. For example 89 is a Disarium number because
# 8^1 + 9^2 = 8 + 81 = 89

def is_disarium(number):
    # Converting the number to a string to loop over its digit
    num_str = str(number)
    # Calculating the sum of digits raised to their respective powers
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))

    # Checking if the sum is equal to the original number
    return digit_sum == number


try:
    num = int(input("Enter a number: "))  # user input

    # Checking if it's a disarium number
    if is_disarium(num):
        print(f"{num} is a Disarium number: ")
    else:
        print(f"{num} is not a disarium number: ")

except ValueError:
    print("Invalid input, please enter a valid number")





