# Sample dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40,
    'e': 50,
}

# Initializing a variable to store the sum
total_sum = 0

# Iterate through the values of the dictionary and add them to the sum
for i in my_dict.values():
    total_sum += i

# display output
print("Sum of all items in the dictionary: ", total_sum)  # 150
