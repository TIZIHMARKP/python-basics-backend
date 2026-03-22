
# ==================== Loops In Python =====================
# ========== While Loops ==============
# The while loop allows you to loop through a certain block of code while a particular feature is true

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# ========== For Loops ==============

mylist = ['ji', 'ju', 'jo']
mydict = {
    'name': 'john',
    'age': 13,
}

for letter in 'Hello':
    print(letter)

for values in mylist:
    if values == 'ju':
        break          # loop stops at ju
    print(values)


for values in mydict:
    print(values)

for x in range(5):
    print(x)

for y in range (3, 7):
    print(y)

for z in range(4):
    print(z)
else:
    print('Finished Looping')