# sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 77, 78, 83, 56]

# Using a list comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("Even numbers in the list are: ", even_numbers)

