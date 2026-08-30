
def is_binary_str(input_str):
    # iterating through each character in the input string
    for i in input_str:
        # checking if the i is not '0' or '1'
        if i not in '01':
            return False  # if any character is not '0' or '1' it's not a binary string

    return True   # if all characters are '0' or '1', it's a binary string

input_str = '1001110'

if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string ")
else:
    print(f"'{input_str}' is not a binary string")



