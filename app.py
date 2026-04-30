# ===========  Assingment 2 ===========

"""
1. Explain the difference between arithmetic. logical and comparison operators in Python.

2. What is operator precedence and why is it important?

3. Describe the difference between the 'is' and '==' operators.

4. What is the function of the modulus operator and where can it be applied?

5. What are f-strings in Python and how are they used?

6. What are the risks of infinite loops and how can they be avoided?

7. Write a program that takes two integer inputs from the user, stores them in variables a and b, and prints the results of addition, subtraction, multiplication, and division.

8. Write a program that takes a user’s score (0–100) as input. If the score is >= 90, print "A"; 80–89, print "B"; 70–79, print "C"; 60–69, print "D"; else print "F". If the score is invalid (<0 or >100), print an error message.

9. Write a program that takes a sentence as input and does the following:

Counts the number of vowels (a, e, i, o, u) using a loop.

Checks if the sentence length is greater than 20 characters and prints a message if true.

Converts the sentence to title case and prints it.

Use a combination of loops, conditionals, and string methods.
"""
# === Solution 1 ===
"""
- Arithmetic operators are used to perform mathematical calculations. They take a number as input and then return a number as output. These operators in python are addition(+), subtraction(-), multiplication(*), division(/), modulus(%), and exponent(**). 
- Logical operators are operators which are used to combine boolean values and also returns a boolean value as the result. They include "and"(both must be True), "or"(at least one must be True) and "not"(reverses the truth value)
- Comparison operators are operators which are always used to compare two values. They always return a boolean result as output. Examples include: ==(equal to), !=(not equal to), >(greater than), <(less than), >=(greater than or equal to) and <=(less than or equal to) 
"""

# === Solution 2 ===
"""
Operator precedence is the rule in which each operator in an expression gets executed first. For example, multiplication is performed first before addition (2 + 3 * 5 equals 17, and not 25). It follows the rules of BODMAS in mathematics
It is important because of the following reasons
- It prevents logical errors, meaning the code might run but still give a wrong answer
- It further removes ambiguity. Without precedence rules, one expression could mean different things and the python interpreter might have to guess the correct expression
- Precedence rules makes code predictable. Since everyone who learns python learns the same rules, any programmer can read your code and know what it is doing 
"""

# === Solution 3 ===
"""
- The "is" is an identity operator while "==" is a comparison operator
- The "is" operator checks if two objects have same identity equality while "==" operator checks if two objects contain the same equality
"""
# === Solution 4 ===
"""
The function of the modulus operator is the get the remainder of a division operation. 
It can be applied to check if a number is even or odd. If number % 2 gives a remainder of 0, then it is an even number else odd number 
"""

# === Solution 5 ===
"""
f-stings is a way to embed variables and expressions directly inside strings. The f stands for formats which makes formatting easier and more readable in a code. Below is an example of how f-strings are used
name = 'Tizih'
school = 'Computer Engineering'
message = f"my name is {name} and I school at {school}"
print(message)
It is used by putting an f before the opening quote and curly braces {} are used to insert variables or expressions in between the opening and closing quote
"""
# === Solution 6 ===



# === Solution 7 ===

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# addition, subtraction, multiplication, division, = a + b, a - b, a * b, a / b
# print(f"Addition of {a} + {b} = {addition}")
# print(f"subtraction of {a} - {b} = {subtraction}")
# print(f"multiplication of {a} * {b} = {multiplication}")
# print(f"division of {a} / {b} = {division}")


# ==== Solution 8 =====

# userScore = int(input("Enter your scroe between 0-100: "))
# if userScore < 0 or userScore > 100:
#     print("Error: Score must be between 0 and 100")
# elif(userScore >= 90):
#     print("A")
# elif(userScore >= 80):
#     print("B")
# elif(userScore >= 70):
#     print("C")
# elif(userScore >= 60):
#     print("D")
# else:
#     print("F")

# ==== Solution 9 ====

vowels = 'aeiouAEIOU'
vowelsCount = 0
sentence = str(input("Enter a sentence: "))

for letter in sentence:
    if letter in vowels:
        vowelsCount += 1
print(f"Number of vowels: {vowelsCount}")

if len(sentence) > 20:
    print("The sentence is longer than 20 characters")

sentenceTitle = sentence.title()
print(f"Title: {sentenceTitle}")