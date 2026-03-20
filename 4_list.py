
# ====================  List In Python =====================
# We can mix different data types in a list

countries = ['United Kingdom', 'Cameroon', 2, True, 'Nigeria', 'Ghana', 'Australia', 'New Zealand']
name = 'Tizih'
print(countries)
print(countries[0])
print(countries[1][1])  # a
print(countries[1:])   # Getting a list from a particular index number to the end
print(countries[2:]) 
print(countries[2:4]) # ['Nigeria', 'Ghana']
countries[0] = 'United States'
countries[4] = 'Canada'
print(countries)
print(countries[-1])     # New Zealand
print(countries[-2])     # Canada
print(len(countries))

# Getting the type of the list
print(type(name))
print(type(countries))
print(type(countries[1]))
print(type(countries[2])) # int
print(type(countries[3])) # bool


# Another way to define a List using the "list constructor"
Countries2 = list(('Nigeria', 35, False))
print(Countries2)
print(type(Countries2))