# Happy Number is a +ve integer that, when you repeatedly replace the number by the sum of the squares of its digits and continue
# the process, eventually it reaches 1. If the process never reaches 1 but instead loops
# endlessly in a cycle, the number is not a Happy Number

# For e.g
# 19 is a Happy Number coz:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# The process reaches 1, so 19 is a Happy Number

def is_happy_numver(num):
    seen = set()    # To Store previously seen numbers 

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))

    return num == 1

num = int(input("Enter a number: "))
if is_happy_numver(num):
    print(f"{num} is a Happy Number")
else:
    print(f"{num} is not a Happy Number")



