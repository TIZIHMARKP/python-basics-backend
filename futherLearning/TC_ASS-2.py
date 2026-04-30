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

# === Solution 7 ===

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
addition, subtraction, multiplication, division, = a + b, a - b, a * b, a / b
print(f"Addition of {a} + {b} = {addition}")
print(f"subtraction of {a} - {b} = {subtraction}")
print(f"multiplication of {a} * {b} = {multiplication}")
print(f"division of {a} / {b} = {division}")

