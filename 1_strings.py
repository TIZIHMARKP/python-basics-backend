# ====================r  Strings =====================
# Strings are just plain text
name = 'Tizih'

print('Hi. \n How are you')
print('Hi. \' How are you') 
print(name[2])
print(name.lower())
print(name.upper())
print(name.islower())
print(name.isupper())
print(name.lower().islower())  # True
print(len(name))               # 5
print(name.index('i')) # getting index of i
print(name.replace('z', 'Z'))