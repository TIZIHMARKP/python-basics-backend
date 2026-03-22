
# ====================  If Statements In Python =====================
# If statement gives a condition for a program to execute the code.

"""
    Example
I write a number
the number is divisible by 2
    then number is an even number
not divisible by 2
    odd number
"""

a = 10
b = 20
c = True
d = 20
boy = True
short = True

if a > b:
    print(f"A = {a} is greater than B = {b}")
else:
    print(f'A = {a} is not greater than B = {b}')

if a == True:
    print("A is true")
else:
    print('A is not true')

if c == False:
    print('C is False')
elif c == True:
    print('C is True')
else:
    print('C is none of the two')

if boy == True or short == True:
    print('He is a boy or he is short')

if boy == True and short == False:
    print('He is a boy or he is short')
else:
    print('None of the two')

# ================== Using ifElse to check for the dataType  =================
value = input('Input a value: ')
if type(value) == str:
    print(value + ' is a string')
elif type(value) == int:
    print(value + ' is an integer')
elif type(value) == list:
    print(value + ' is a list')
else:
    print('We don\'t know the data type of ' + value)

# ================== Checking if a number is divisible by 5  =================
number = int(input('Input a number: '))

if number%5 == 0:
    print(number, 'can be divided by 5')
else:
    print(number, 'can not be divided by 5')

# ================== Checking if the length of a sentence is less than 10  =================
sentence = input('Enter a sentence: ')
if len(sentence) < 10:
    print('The Sentence: \"' +sentence+ '\" is less than 10')
else: 
    print('The Sentence: \"' +sentence+ '\" is greater than 10')



 


