# Python Program to check if a string contains any special character

import re

def check_special_char(in_str):

    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'

    if re.search(pattern, in_str):
        return True
    else:
        return False

