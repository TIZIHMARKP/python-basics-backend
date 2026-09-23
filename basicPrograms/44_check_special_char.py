# Python Program to check if a string contains any special character

import re

def check_special_char(in_str):
    # Defining special regular expression pattern to match special characters
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'
    # Using re.search to find a match in the input string
    if re.search(pattern, in_str):
        return True
    else:
        return False

    

