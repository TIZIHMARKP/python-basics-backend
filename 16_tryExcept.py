
# ==================== Try Except In Python =====================
#  The try Except in python prevents and error from occuring in the code.

# try:
#     x = int(input('Input an integer: '))
#     print(x)
# except:
#     print('Something went wrong... Please try again')

# Incase of value error:

try:
    y = int(input('Input an integer: '))
    print(y)
except ValueError:
    print('Value not a integer2')


try:
    z = int(input('Input an integer: '))
    print(y)
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')

try:
    a = int(input('Input an integer: '))
    print(a)
except:
    print('Something went wrong')
finally:
    print('Try except finished: ')   # Runs if there is a problem or not
