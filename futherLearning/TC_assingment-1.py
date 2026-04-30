
# ====================  Assingment: Task 1 =====================

# === Number 7: that declares three variables name, age, and height with appropriate data types (string, integer, float) and assigns them values. Print each variable on a new line.

# name = 'Tizih'
# age = 120
# height = 1.8

# print('Name = ' +name + '\nAge = ', age, '\nHeight = ', height)

# === No 8: Write a program that declares a string variable num_str = "123". Convert it to an integer, add 50 to it, and print the result. Then, convert the result back to a string and print its type.

# num_str = '123'
# integerNum = int(num_str)
# Sum = integerNum + 50
# print(Sum)
# result = str(Sum)
# print('Type of result after converting to string: ', type(result))

# === No 9: Store three variables: product = "Laptop", price = 999.99, and quantity = 3. Print a single sentence like: "Buying 3 Laptops costs $2999.97." (Calculate total cost dynamically.)

# product = "Laptop"
# price = 999.99
# quantity = 3
# totalPrice = price * quantity

# print('Buying',quantity, f'Laptops costs ${totalPrice:.2f}')

# === No 10: Create a program that declares a variable score with an initial value of 100. Then, overwrite it with a string "High Score" and finally with a boolean True. Print the value and type of score after each assignment

# option 1
score = 100
values = [100, 'High Score', True]

for val in values:
    score = val
    print(score, ':', type(score))

# option 2
# score = 100
# print(f"{score} : {type(score)}")
# score = 'High Score'
# print(f"{score} : {type(score)}")
# score = True
# print(f"{score} : {type(score)}")




