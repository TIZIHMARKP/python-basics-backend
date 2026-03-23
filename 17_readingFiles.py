
# ==================== Reading Files =====================
# continue at 03:00

countryFile = open('countries.txt', 'r')   # w(write on the file), a(Append on the file), r+(we want to do both reading and writing) 

print(countryFile.readable())
# print(countryFile.readline())      # Prints the first line: Cameroon
# print(countryFile.readline())      # Prints the 2nd line England
# print(countryFile.readlines())     # Prints all the lines in the file
# print(countryFile.readlines()[1])      # Prints the second line

for lines in countryFile.readlines():
    print(lines)


countryFile.close()