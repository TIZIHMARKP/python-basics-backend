
key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# Initializing an empty dictionary
flat_dict = {}

# Iterate through the list and add key-value pairs to the dictionary
for key, value in key_values_list:
    flat_dict[key] = value

# print the resulting flat dictionary
print("Flat Dictionary: ", flat_dict)
