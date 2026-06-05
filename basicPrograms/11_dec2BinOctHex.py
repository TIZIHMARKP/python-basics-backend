# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

# Converting a decimal number to binary, octal, and hexadecimal involves dividing the
# decimal number by the base repeatedly and noting the remainders at each step. For e.g:

# Binary = base 2
# Octal = base 8
# hexadecimal = base 16


dec_num = int(input("Enter a decimal Number: "))

print("The decimal value of: ", dec_num, "is: ")
print(bin(dec_num), "In binary")
print(oct(dec_num), "In octal")
print(hex(dec_num), "In hexadecimal")








