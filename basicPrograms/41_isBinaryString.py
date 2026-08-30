
def is_binary_str(input_str):

    for i in input_str:

        if i not in '01':
            return False

    return True

input_str = '0110101'



