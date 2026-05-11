
# ====================  Functions In Python =====================
# Function is a block of code which performs a particular task
 
def greetingsFunction():
    print('Welcome Tizih')

def greetingsFunction1(name, age):
    print('Welcome ' +name+ '.You have a life span of ', age, ' years.')

def greetingsFunction2(*names):  # Passing in more than 1 value we make use of "*"
    print('Welcome ' +names[1])

def greetingsFunction3(name, age):
    print('Welcome ' +name+ '.You are ', age, ' years old.')

name = input('Enter your name: ')
age = input('Enter your age: ')

greetingsFunction()
greetingsFunction1('Mark Marko', 120)
greetingsFunction2('Prince', 'Royal', 'Paul')
greetingsFunction3(name, age)


