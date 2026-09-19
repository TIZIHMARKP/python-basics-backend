
def find_duplicates(input_str):
    # creating an empty dictionary to store character counts
    char_count = {}
    # Initializing a list to store duplicate chars
    duplicates = []
    # Iterating through each character in the input string
    for i in input_str:
        # If char already in dict, we increment its count
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    # we iterate through the dict & add characters with count > 1
    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)

    return duplicates

# Input string
input_string = 'royal shiloh'

# finding the duplicate char in string
duplicate_chars = find_duplicates(input_string)

print("Duplicate characters: ", duplicate_chars)   # ['o', 'l']



